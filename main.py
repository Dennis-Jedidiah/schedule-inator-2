import Constants
import sys
from icalendar import Calendar, Event
from datetime import datetime

if len(sys.argv) < 2:
    raise Exception("No filename provided")

# Takes the input file's name as an argument.
fileName = sys.argv[1]

originalFile = open(fileName, 'r')
cleanedData = Constants.clean_input(originalFile.read())
currentCourse = ""
listOfCourses = []

# This loop goes through each line of the cleaned data and extracts course information.
# and puts it into a list of Course objects.
for line in cleanedData.splitlines():
    if "END_OF_COURSE" in line:
        course_name = Constants.extract_course_name(currentCourse)
        course_code = Constants.extract_course_code(currentCourse)
        section = Constants.extract_section(currentCourse)
        crn = Constants.extract_crn(currentCourse)
        start_date = Constants.extract_start_date(currentCourse)
        end_date = Constants.extract_end_date(currentCourse)
        location = Constants.extract_location(currentCourse)
        type_ = Constants.extract_type(currentCourse)
        method = Constants.extract_method(currentCourse)
        day = Constants.extract_days(currentCourse)
        start_time = Constants.extract_start_times(currentCourse)
        end_time = Constants.extract_end_times(currentCourse)
        instructor = Constants.extract_instructor(currentCourse)
        building = Constants.extract_building(currentCourse)
        room = Constants.extract_room(currentCourse)
        listOfCourses.append(Constants.Course(
            name=course_name,
            code=course_code,
            section=section,
            crn=crn,
            start_date=start_date,
            end_date=end_date,
            location=location,
            type_=type_,
            method=method,
            days=day,
            start_times=start_time,
            end_times=end_time,
            instructor=instructor,
            building=building,
            room=room
        ))
        currentCourse = ""
    else:
        currentCourse += line + "\n"
originalFile.close()

# This part creates the .ics file using the list of Course objects.
cal = Calendar()
cal.add('prodid', '-//Schedule-inator//Dennis_Jedidiah//')
cal.add('version', '2.0')
for course in listOfCourses:
    for i in range(len(course.days)):
        event = Event()
        event.add('summary', f"{course.name}")
        event.add('location', course.location)
        event.add('description', f"Instructor: {course.instructor} \n Course Code: {course.code} \n Method: {course.method} \n CRN: {course.crn}")
        event.add('dtstart', Constants.parse_date_time(course.start_date, course.start_times[i] if course.start_times else ""))
        event.add('dtend', Constants.parse_date_time(course.start_date, course.end_times[i] if course.end_times else ""))
        event.add('rrule', {'freq': 'weekly', 'byday': (course.days[i])if course.days else "Monday", 'until': Constants.parse_date_time(course.end_date, course.end_times[i] if course.end_times else "")})
        cal.add_component(event)

with open("class_schedule.ics", "wb") as f:
    f.write(cal.to_ical())