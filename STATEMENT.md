#  Problem Statement & Project Scope

## Problem Statement
Traditional methods of tracking student attendance, such as paper registers or generic spreadsheets, are inefficient and prone to administrative errors. These methods lack real-time visibility and make it difficult for educators to quickly generate an attendance summary. The need is for a **simple, dedicated, and durable desktop application** that centralizes attendance logging, ensures data integrity, and provides immediate cumulative attendance metrics.

## Scope of the Project
The **Student Attendance Manager (SAM)** project is defined as a standalone, desktop utility built on Python and Tkinter. The project's scope focuses on providing essential CRUD (Create, Read, Update, Delete) functionality for attendance data.

### Functional Requirements Met by Scope:
1.  **User Management Module:** Function to add new student records.
2.  **Data Processing Module:** Functions to increment Present/Absent counts.
3.  **Reporting/Analytics Module:** Visualization of cumulative Present and Absent totals in the main GUI.

### Inclusions:
* Local data persistence using JSON file storage.
* Basic error handling for input and file operations.
* Intuitive GUI for ease of use.

### Exclusions (Future Scope):
* Network/database integration (e.g., MySQL, PostgreSQL).
* Time-stamping of individual attendance marks (only cumulative count is maintained).
* Complex report generation (e.g., monthly attendance percentages).

## Target Users
The primary beneficiaries and target users of the Student Attendance Manager are:
1.  **Teachers and Professors:** Who require a straightforward, digital register for quickly marking attendance during class sessions.
2.  **Teaching Assistants (TAs):** Responsible for tracking attendance in labs, practicals, or discussion groups.
3.  **Small Group Coordinators:** Who need an easy way to manage participation metrics for project teams or clubs.

## High-Level Features
The application provides the following core capabilities to fulfill its objective:
1.  **Registration:** The ability to add new student entries to the tracking system.
2.  **Marking:** The ability to mark a registered student as either 'Present' or 'Absent' for one session.
3.  **Viewing:** A real-time, tabulated view of all students and their current total Present and Absent counts.
4.  **Serialization:** The capability to save the structured attendance data to a local file and load it back correctly upon application launch.
