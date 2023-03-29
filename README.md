# Hospital Database Management System

The system is designed to manage the day-to-day operations and processes of a hospital. The database schema of the system consists of different tables such as patient, doctor, appointment, medical history, diagnosis, and billing. Each of these tables holds relevant information that is required for hospital operations. 

The system provides an interface that allows to manage and view the data efficiently. One can access and update patient information, schedule appointments, and generate bills(using functions/procedures and triggers). The system provides a view features that allows staff to quickly find patient data, medical histories, and diagnosis information.

## Tables Featured:

Staff(**s_id**, s_name, salary, *retirement_date, date_joining)
- Doctor(**s_id**, department, )
- Nurse(**s_id**, seniority, department)
- Non-Medical Staff(**s_id**, Duty type)

Patient(**p_id**,p_name, gender, address, phone no.,)
- Patient History(**p_id**, **a_id**) 
- Room(**r_no**, r_type, r_fee_per_day, *Nurse1(s_id)*, *Nurse2(s_id)*) //Here, s_id indicates nurse alloted to that patient
- Billing(**b_no**, **p_id**, date, Diagnosis cost, a_id, Medicine Cost, Procedure cost, Total cost)

Appointment(**a_id**, p_id, s_id, date)
- Procedure(**a_id**, **date_admit**, r_no, *date_discharge*, details)
- Diagnosis(**a_id**, b_no, diagnosis, medicine)

## Some Definitions:
- We distinguish between the nurse, doctors, and Non_medical members alloting s_id such that it begins with keyword DOC for doctors, NUR for nurses, and NMS for Non medical staff.
- We can say that the Doctor with ID DOC0000 will be deemed administrator with total control over the database.
- Some tables such as Staff, Patient, Patient History, Billings, cannot be deleted, and can only be updated with new data.
- Bold signifies Primary Key, whereas italics signify NULL allowed.