from datetime import datetime
import re

## REGEX PATTERNS
COURSENAMEMATCH = "([A-z\.\,\-\& ]+)(?=\n[0-9A-z ]+Section [0-9]+)"
COURSECODEMATCH = "([0-9A-z ]+)Section [0-9]+"
SECTIONMATCH = "(Section [0-9]+)"
DAYSOFTHEWEEK = "S\nM\nT\nW\nT\nF\nS\n"
COURSESTARTDATE = "Class Begin: ([0-9/]+)"
COURSEENDDATE = "Class End: ([0-9/]+)"
COURSELOCATION = "Campus: ([A-z\,\-\& ]+)"
COURSETYPE = "Schedule Type: ([A-z \,\-\&]+)"
COURSEMETHOD =  "Instructional Method: ([A-z \,\-\&]+)"
COURSEDAY = "[0-9/]+ +-- +[0-9/]+ +([A-z]+)"
COURSESTARTTIME = " +([0-9: ]+[PAM]{2}) -"
COURSEENDTIME = "-([0-9: ]+[PAM]{2})"
COURSEINSTRUCTOR = "Instructor: ([A-z\,\-\|\& ]+)"
COURSEBUILDING = "Building: ([A-z\,\-\|\& ]+)"
COURSEROOM = "Room: ([A-z\,\-\|\& \d]+)"
DAYSDICTIONARY = {
    "Monday": "MO",
    "Tuesday": "TU",
    "Wednesday": "WE",
    "Thursday": "TH",
    "Friday": "FR",
    "Saturday": "SA",
    "Sunday": "SU",
    "None"  : "MO"  # Default to Monday if no days are found
}

## CLASSES
class Course:
    def __init__(self, name="", code="", section="", crn="", start_date="", end_date="", location="", type_="", method="", days=None, start_times=None, end_times=None, instructor="", building="", room=""):
        self.name = type_ + " - " + name
        self.code = code
        self.section = section
        self.crn = crn
        self.start_date = start_date
        self.end_date = end_date
        self.location = location + " " + building + " " + room
        self.method = method
        self.days = [DAYSDICTIONARY[day] for day in days]
        self.start_times = start_times if start_times is not None else []
        self.end_times = end_times if end_times is not None else []
        self.instructor = instructor

## FUNCTIONS
def clean_input(text: str) -> str:
    # Remove leading and trailing whitespace
    cleaned = text.strip()
    dateRemoved = re.sub(DAYSOFTHEWEEK,"",cleaned)
    dateRemoved = re.sub("\|", "\n", dateRemoved)
    dateRemoved = re.sub(r"(CRN: [0-9]*)", r"\1\nEND_OF_COURSE", dateRemoved)
    return dateRemoved
def extract_course_name(text: str) -> str:
    match = re.search(COURSENAMEMATCH, text)
    if match:
        return match.group(1).strip()
    return "Course Name Not Found"
def extract_course_code(text: str) -> str:
    match = re.search(COURSECODEMATCH, text)
    if match:
        return match.group(1).strip()
    return "Course Code Not Found"
def extract_section(text: str) -> str:
    match = re.search(SECTIONMATCH, text)
    if match:
        return match.group(1).strip()
    return "Section Not Found"
def extract_crn(text: str) -> str:
    match = re.search(r"CRN: ([0-9]+)", text)
    if match:
        return match.group(1).strip()
    return "CRN Not Found"
def extract_start_date(text: str) -> str:
    match = re.search(COURSESTARTDATE, text)
    if match:
        return match.group(1).strip()
    return "Start Date Not Found"
def extract_end_date(text: str) -> str:
    match = re.search(COURSEENDDATE, text)
    if match:
        return match.group(1).strip()
    return "End Date Not Found"
def extract_location(text: str) -> str:
    match = re.search(COURSELOCATION, text)
    if match:
        return match.group(1).strip()
    return "Location Not Found"
def extract_type(text: str) -> str:
    match = re.search(COURSETYPE, text)
    if match:
        return match.group(1).strip()
    return "Type Not Found"
def extract_method(text: str) -> str:
    match = re.search(COURSEMETHOD, text)
    if match:
        return match.group(1).strip()
    return "Method Not Found"
def extract_days(text: str) -> list[str]:
    matches = re.findall(COURSEDAY, text)
    return [match.strip() for match in matches]
def extract_start_times(text: str) -> list[str]:
    matches = re.findall(COURSESTARTTIME, text)
    return [match.strip() for match in matches]
def extract_end_times(text: str) -> list[str]:
    matches = re.findall(COURSEENDTIME, text)
    return [match.strip() for match in matches] 
def extract_instructor(text: str) -> str:
    match = re.search(COURSEINSTRUCTOR, text)
    if match:
        return match.group(1).strip()
    return "Instructor Not Found"
def extract_building(text: str) -> str:
    match = re.search(COURSEBUILDING, text)
    if match:
        return match.group(1).strip()
    return "Building Not Found"
def extract_room(text: str) -> str:
    match = re.search(COURSEROOM, text)
    if match:
        return match.group(1).strip()
    return "Room Not Found"
def parse_date_time(date_string: str, time_string: str) -> datetime:
    if not time_string:
        time_string = "12:00 AM"
    combined_string = f"{date_string} {time_string}"
    return datetime.strptime(combined_string, "%m/%d/%Y %I:%M %p")