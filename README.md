#  Student Attendance Manager (SAM)

## Project Title
**Student Attendance Manager (SAM):** A Simple, Desktop GUI Application

## Overview of the Project
The **Student Attendance Manager (SAM)** is a utility designed for educators and administrators to efficiently manage and track student attendance records. Developed using **Python** and the **Tkinter** library, this application provides a user-friendly Graphical User Interface (GUI) that replaces manual attendance logs. It allows users to register students, mark their presence or absence for a session, and securely persist the cumulative attendance data using local JSON file storage.

## Key Features (High-Level)
* **User Management (Add):** Quickly register new student names into the system.
* **Session Tracking (Mark):** Mark individual students as either **Present** or **Absent** for a session, updating their cumulative counts.
* **Data Persistence (Load/Save):** Automatically loads records on startup and securely saves all attendance data to an `attendance.json` file.
* **Real-time Summary:** Displays an immediate, sortable table (Treeview) showing each student's name, total days **Present**, and total days **Absent**.

##  Technologies & Tools Used
* **Primary Language:** Python 3.x
* **GUI Library:** `tkinter` and `tkinter.ttk` (Standard Python libraries)
* **Data Persistence:** `json` module for File I/O (JSON serialization/deserialization)
* **Version Control:** Git

##  Steps to Install & Run the Project

This project requires a standard Python 3 environment.

### Prerequisites
1.  Ensure you have **Python 3.x** installed.
2.  `tkinter` is typically included with standard Python installations.

### Running the Application
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/kashyap10101/student_attendance_manager
    cd Attendance_Manager
    ```
2.  **Execute the Script:**
    ```bash
    python attendance_manager.py
    ```
    *Note: The script will automatically create the `attendance.json` file in the same directory upon its first execution if it doesn't already exist.*

##  Instructions for Testing
To confirm the application is fully functional, perform the following validation tests:

1.  **Student Registration Test:**
    * Click the **Add** button and input "Priya".
    * Verify "Priya" appears in the main table with Present: 0 and Absent: 0.
2.  **Marking Functionality Test:**
    * Use the **Mark** button. Select "Priya".
    * Mark "Priya" as **Present**. The table must update instantly to Present: 1.
    * Use the **Mark** button again. Select "Priya".
    * Mark "Priya" as **Absent**. The table must update instantly to Absent: 1.
3.  **Data Persistence Test (Crucial):**
    * Click the **Save** button (or exit and choose 'Save').
    * Close the application and restart it.
    * The table must load with "Priya" showing Present: 1 and Absent: 1.
4.  **Error Handling Test:**
    * Try adding a student whose name is already present (e.g., "Priya"). The system must show a warning message ("Already got that one") and prevent duplication.
<img width="1333" height="697" alt="image" src="https://github.com/user-attachments/assets/7c4ce019-3a9c-4fe6-b3f4-2e7ec10994f5" />
<img width="1221" height="617" alt="image" src="https://github.com/user-attachments/assets/6cee493f-2325-4d5a-bc29-4a8d2a49099d" />
<img width="923" height="610" alt="image" src="https://github.com/user-attachments/assets/51d2099e-1b32-446d-b07d-2173c790bd84" />
<img width="923" height="610" alt="image" src="https://github.com/user-attachments/assets/58d1588f-81c3-4a90-aeab-c1f324746683" />


