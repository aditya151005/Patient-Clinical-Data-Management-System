# Patient-Clinical-Data-Management-System
Patient Clinical Data Management System is a web application developed using HTML, CSS, Python, Django and database used is MySQL.
User Story 1
As a lab assistant, I want to view all the patients records.
Acceptance Criteria-
1.Display all the patients details with their id,firstName,lastName,age.
2.Display the link to enter clinical data for each patient.
3.Display the link to analyze data for each patient.
4.Display the link to register new patients.
User Story 2
As a lab assistant , I want to register a new patient
Acceptance Criteria-
On click of the Add Patient link the user should be navigated to the patient registration screen.
The user should see a form that he can fill in with patient details namely firstName,lastName,age.
When the user click the confirm button the data should be be saved and a confirmation message should bed displayed.
The user should be able to navigate back to the home page.
User Story 3
As a lab assistant, I want to enter clinical data for a patient
Acceptance Criteria-
On click of the Add Data link on the home page the user should be navigated to the clinical data entry screen.
The user should see a form that can fill in with patient details such as bp ,height,weight and heart rate.
When the user click the confirm button the data should be saved and a confirmation message should be displayed.
The user should be able to navigate back to the home page.
User Story 4
As a lab assistant,I want to analyze and see a report of the latest tests-
Acceptance Criteria-
On click of the Analyze Data link on the home page the user should be navigated to page where he can see the latest entries for various clinical data.
The Body Mass Index should be displayed based on height and weight of the patient.
Main tables in Patient Clinical Data Management System -
1.Patient Details  (one to many relationship)  2.Patient Clinical Data Management System project work flow-
  1.All the users have credentials(username and password) to login into the system.
  2.Allow the end users(lab assistants) to do CRUD(create,read,update,delete) operations on patient data. we use class based view to perform CRUD operations.
  3.Application also has the facility of adding and analyzing clinical data. To perform these operation, we use function based view.

