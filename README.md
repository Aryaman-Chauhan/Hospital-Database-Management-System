# Hospital Database Management System

The system is designed to manage the day-to-day operations and processes of a hospital. The database schema of the system consists of different tables such as patient, doctor, appointment, medical history, diagnosis, and billing. Each of these tables holds relevant information that is required for hospital operations. 

The system provides an interface that allows you to manage and view the data efficiently. One can access and update patient information, schedule appointments, and generate bills (using functions/procedures and triggers). The system provides a view feature that allows staff to quickly find patient data, medical histories, and diagnosis information.

## ER Diagram: 

![Library Management System](https://github.com/Aryaman-Chauhan/Hospital-Database-Management-System/blob/main/Images/ERDiagram.png)

## Tables Featured:

Staff(**s_id**, s_name, salary, retirement, joining, Ph.No., Address, Gender, password)
- Department(**dep_id**, Dep_name)
- Doctor(**s_id**, dep_id)
- Nurse(**s_id**, seniority, dep_id)
- Non-Medical Staff(**s_id**, duty_type)

Patient(**p_id**,p_name, gender, address, phone no.,password)
- Room(**r_no**, r_type, room_fee_per_day, *Nurse_1(s_id)*, *Nurse_2(s_id)*, status) //Here, s_id indicates nurse alloted to that patient
- Billing(**b_no**, a_id, p_id, date, Diagnosis cost, Medicine Cost, Procedure cost, Total cost)

Appointment(**a_id**, p_id, s_id, date,status)
- Procedure(**a_id**, date_admit, *r_no*, *date_discharge*, details)
- Diagnosis(**a_id**, **b_no**, diagnosis, medicine)

## Functional Dependencies

- Staff{s_id -> s_name, salary, retirement, joining, Ph.No., Address, password, gender}
- Departments{dep_id -> dep_name}
- Doctor{s_id -> dep_id}
- Nurse{s_id -> seniority, dep_id}
- Non-Medical staff{s_id -> duty_type}
- Diagnosis{a_id, b_no -> Diagnosis, Medicine}
- Appointment{a_id -> p_id, s_id, date, status}
- Procedure{a_id,date -> date_discharge,r_no,details}
- Room{r_no -> r_type, room_fee_per_day, *nurse_1*,*nurse_2*,status}
- Billing{b_no -> a_id, p_id,date,diagnosis_cost, medicine_cost,procedure_cost, total_cost}
- Patient{p_id -> p_name,gender, Ph.No., Address, password}

The 1NF is guaranteed using nurse_1, nurse_2 in Room, which allows us to allot more than one nurse to a single room.

The 2NF is allowed by the fact that primary keys are chosen such that they're always unique, so this shows that there are no partial dependencies. This is further explained in the video.

The 3NF is maintained as there are no transitive dependencies. The primary key alone can determine the row table selected.

## Some Definitions:
- We distinguish between the nurse, doctors, and Non_medical members alloting s_id such that it begins with keyword DOC for doctors, NUR for nurses, and NMS for Non medical staff.
- We can say that the Doctor with ID DOC0000 will be deemed administrator with total control over the database.
- Some tables such as Staff, Patient, Patient History, Billings, cannot be deleted, and can only be updated with new data.
- Bold signifies Primary Key, whereas italics signify NULL allowed.
