# schedule-inator-2

**schedule-inator-2** is a Python-based tool designed to convert your OTU course registration information into a calendar schedule.

## Features

- Read and parse schedules from a text file
- Command-line interface for interacting with your schedule
- Easy setup and usage

## Getting Started

### Prerequisites

- Python 3.9 or higher (recommended)
- `pip` for installing dependencies

### Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd schedule-inator-2
   ```
   or
   ```
   Click code, download zip, then extract the folder to where you want.
   Then open the folder in your terminal.
   ```

2. **(Optional) Create a virtual environment:**  
    Mac:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
    Windows
    ```ps
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   or
   ```
   pip3 install -r requirements.txt
   ```

### Configuration

- Ensure your schedule is in the `my_schedule.txt` file in the project root.
- You can modify `Constants.py` to adjust any default settings.

## Usage
To get your course registration info:

- Go to [MyOntarioTech](https://my.ontariotechu.ca/) and click Undergraduate/Graduate student.  
- Click the "My Academics" Dropdown.
- Click on the "My Course Schedule" on the left side of the screen.
- Select the current/wanted term
- Click schedule details near the bottom half of the page
  ![Schedule Details](https://github.com/user-attachments/assets/e55472a4-cc75-4eeb-b862-3540e6f1840b)
- Click the Up button
  ![Up button](https://github.com/user-attachments/assets/241a9899-dd6b-41ab-b157-f0cecf5b3516)
- Click the dropdown arrow on all your courses
  ![Dropdown](https://github.com/user-attachments/assets/ea513273-d2a6-4f71-8308-94b5f89c9424)
- Click and drag to select everything in the Schedule Details section, then copy it into a file named `my_schedule.txt` (or whatever you want) and save that file in the same location as the `main.py` file.


To run the application, use:

```sh
python3 main.py my_schedule.txt
```
or
```sh
python main.py my_schedule.txt
```

This will start the program and load your schedule from `my_schedule.txt`.

### Example Schedule File

Your `my_schedule.txt` should be formatted as follows:

```
Astronomy I | Physics 2900U Section 001 | Class Begin: 09/02/2025 | Class End: 12/01/2025
Registered
Message: **Web Registered** | Hours: 3 | Level: Undergraduate | Campus: OT-North Oshawa | Schedule Type: Lecture | 
...
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

