import sys
import re
import Constants

# if len(sys.argv) < 2:
#     raise Exception("No filename provided")

# Takes the input file's name as an argument.
# fileName = sys.argv[1]
fileName = "my_schedule.txt"
# for testing purposes. testing out the file cleaning process.
originalFile = open(fileName, 'r')
data = originalFile.read()
cleanedData = Constants.clean_input(data)
currentCourse = ""
for line in cleanedData.splitlines():
    if "END_OF_COURSE" in line:
        # print(f"Current Course Data:\n{currentCourse}")
        print("----- End of Course -----")

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
            # Print extracted details for verification
        print(f"Course Name: {course_name}")
        print(f"Course Code: {course_code}")
        print(f"Section: {section}")
        print(f"CRN: {crn}")
        print(f"Start Date: {start_date}")
        print(f"End Date: {end_date}")
        print(f"Location: {location}")
        print(f"Type: {type_}")
        print(f"Method: {method}")
        print(f"Day: {day}")
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Building: {building}")
        print(f"Room: {room}")
        print(f"Instructor: {instructor}")
        print("------------------------\n")
        currentCourse = ""
    else:
        currentCourse += line + "\n"
originalFile.close()
# This loop reads through the input file line by line and recognizes the end of a course description.
# with open(fileName, 'r') as file:
#     course_number = 1
#     for line in file:
#         if "CRN" in line:
#             course_number += 1

# print(course_number)