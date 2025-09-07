import re

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
