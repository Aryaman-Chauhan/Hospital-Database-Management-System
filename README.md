"# Hospital-Database-Management-System" 

The system is designed to manage the day-to-day operations and processes of a hospital. The database schema of the system consists of different tables such as patient, doctor, appointment, medical history, diagnosis, and billing. Each of these tables holds relevant information that is required for hospital operations. 

The system provides an interface that allows to manage and view the data efficiently. One can access and update patient information, schedule appointments, and generate bills(using functions/procedures and triggers). The system provides a view features that allows staff to quickly find patient data, medical histories, and diagnosis information.

Tables Featured:

Staff(**s_id**, s_name, salary, date_joining)
- Doctor(**s_id**, department, )
- Nurse(**s_id**, )
- Non-Medical Staff(**s_id**, )

Patient(**p_id**,p_name, gender)
- Patient History(**p_id**, date_admit, b_no)
- Room(**r_no**, r_type, r_fee_per_day)
- Billing(**b_no**, **p_id**, date, cost, )

Appointment
- Procedure
- Diagnosis