Select `password` from patient where p_id='{PatientLogin.ids}';

insert into PATIENT (p_name,gender,address,`Ph.No.`,`password`) VALUES('{name}','{gndr}','{adr}','{phnum}','{pwd1}');

SELECT p_id from patient order by p_id desc limit 1;

update staff set retirement='{date}' where s_id='{id}';

update staff set `password` = '{newpass}' where s_id='DOC0000';

select s_id, s_name, joining, `Ph.No.`, Address, Gender, Salary from staff order by s_id;

select p_id, p_name, `Ph.No.`, Address, Gender from patient;

UPDATE STAFF SET SALARY={chansal} WHERE s_id='{chanid}';

insert into room(r_type, room_fee_per_day) values('{dept}',{fee});

insert into departments(dep_name) values('{dept}');

select convert(substring(s_id,4,4),unsigned) + 1 from doctor order by s_id desc limit 1;

INSERT INTO Doctor(s_id, dep_id) values (concat('DOC',LPAD({s_id},4,0)),{spec});

Insert into staff(s_id,s_name,salary,joining,`Ph.No.`,Address, `password`, gender) select s_id,'{name}', {salary}, current_date, '{phnum}', '{adr}', '{pwd1}', '{gndr}' from doctor order by s_id desc limit 1;

select convert(substring(s_id,4,4),unsigned) + 1 from nurse order by s_id desc limit 1;

INSERT INTO Nurse(s_id, dep_id, seniority) values (concat('NUR',LPAD({s_id},4,0)),{spec}, '{senior}');

Insert into staff(s_id,s_name,salary,joining,`Ph.No.`,Address, `password`, gender) select s_id,'{name}', {salary}, current_date, '{phnum}', '{adr}', '{pwd1}', '{gndr}' from nurse order by s_id desc limit 1;

select convert(substring(s_id,4,4),unsigned) + 1 from `non-medical staff` order by s_id desc limit 1;

INSERT INTO `Non-Medical Staff`(s_id, duty_type) values (concat('NMS',LPAD({s_id},4,0)),'{dutype}');

Insert into staff(s_id,s_name,salary,joining,`Ph.No.`,Address, `password`, gender) select s_id,'{name}', '{salary}', current_date, '{phnum}', '{adr}', '{pwd1}', '{gndr}' from `Non-Medical Staff` order by s_id desc limit 1;

Select dep_name from departments;

select p.p_id,p.p_name,p.gender,p.address,p.`Ph.No.` from patient as p where p.p_id={PatientLogin.ids};

update patient set `Ph.No.` = '{newPh}' where p_id='{PatientLogin.ids}';

update patient set `password` = '{newpass}' where p_id='{s_id}';

Select a.a_id,a.s_id,s.s_name,dep.dep_name,a.date,a.status from appointment as a join doctor as d using(s_id) join departments as dep using(dep_id) join staff as s using(s_id) where p_id ='{PatientLogin.ids}';

select dep_id from departments where dep_name='{dept}';

insert into appointment(p_id, s_id, date) select {PatientLogin.ids},s_id,date_add(current_date(),interval 3 day) from doctor where dep_id = {depid} and s_id<>'DOC0000' order by rand() limit 1;

select a_id from appointment where p_id={PatientLogin.ids} order by a_id desc limit 1;

select a_id from appointment where p_id={PatientLogin.ids} order by a_id desc limit 1;

Update appointment  Set status = 'cancelled' where a_id ={PatientPage.aid} and p_id={PatientLogin.ids} and status='Pending';

select a_id from appointment where p_id={PatientLogin.ids} order by a_id desc limit 1;

Update appointment Set status = 'diagnosis' where a_id ={PatientPage.aid} and p_id={PatientLogin.ids} and status='Pending';

Insert into billing(p_id,date,a_id) values({PatientLogin.ids},current_date,{PatientPage.aid});

Insert into diagnosis(a_id,b_no,diagnosis,medicine) select {PatientPage.aid},b.b_no,'','' from billing as b where b.p_id={PatientLogin.ids} and b.a_id={PatientPage.aid};

select a_id from appointment where p_id={PatientLogin.ids} order by a_id desc limit 1;

Update appointment  Set status = 'procedure' where a_id ={PatientPage.aid} and p_id={PatientLogin.ids} and status='diagnosis';

insert into `procedure`(a_id,date) values({PatientPage.aid},current_date);

select diagnosis, medicine from diagnosis join appointment using(a_id) where a_id = {aid} and (status='Diagnosis' or status='Procedure' or status='Completed');

select details from `procedure` join appointment using(a_id) where a_id = {aid} and (status='Procedure' or status='Completed');

select b.a_id,b.b_no,b.p_id,b.diagnosis_cost,b.medicine_cost,b.procedure_cost,b.total_cost,a.status from billing as b join appointment as a using(a_id) where a.p_id={PatientLogin.ids};

select dep_name from departments join doctor using(dep_id) where s_id<>'DOC0000' group by dep_id;

select s.s_id,s.s_name,s.salary,s.joining,d.dep_name,s.address,s.`Ph.No.` from doctor join staff as s using(s_id) join departments as d using (dep_id) where  s_id = '{StaffLogin.ids}';

select a_id,p_id,patient.p_name,date from appointment join patient using(p_id) where s_id = '{StaffLogin.ids}' and status ='diagnosis';

select a_id,p_id,patient.p_name,date,status from appointment join patient using(p_id) where s_id = '{StaffLogin.ids}' and (status ='procedure' or status='diagnosis');

SELECT p_id, p_name, gender, address, `Ph.No.` from Patient where p_name LIKE '%{checkpat}%';

SELECT p_id, p_name, gender, address, `Ph.No.` from Patient where p_id = '{checkid}';

update diagnosis join appointment using(a_id) set diagnosis = concat(diagnosis,CHAR(13, 10),current_time, '{diag}'), medicine = concat(medicine,CHAR(13, 10),current_time,'{med}') where a_id = {aid} and status='diagnosis' and s_id='{StaffLogin.ids}';

update `procedure` join appointment using(a_id) set details = concat(details,CHAR(13, 10),current_time, '{det}') where a_id = {aid} and status='procedure' and s_id='{StaffLogin.ids}';

select a.a_id,a.p_id,p.p_name,a.date,a.status from appointment as a join patient as p using(p_id) where s_id = '{StaffLogin.ids}';

select s.s_id,s.s_name,s.salary,n.seniority,s.joining,d.dep_name,s.address,s.`Ph.No.` from nurse as n join staff as s using(s_id) join departments as d using (dep_id) where  s_id = '{StaffLogin.ids}';

select r_no,r_type from room where nurse_1 = '{StaffLogin.ids}' or nurse_2='{StaffLogin.ids}';

select a.a_id,r.r_no,r.r_type,p.p_id,p.p_name,p.gender from patient as p join appointment as a using(p_id) join `procedure` using(a_id) join room as r using(r_no) where r.nurse_1='{StaffLogin.ids}' or r.nurse_2='{StaffLogin.ids}';

select a.a_id,a.p_id, ss.s_name,d.b_no,d.diagnosis,d.medicine,a.date,p.date,p.r_no,p.details from appointment as a join `procedure` as p using(a_id) join diagnosis as d using(a_id) join staff as ss using(s_id) where a_id = {apid};

select s.s_id,s.s_name,s.salary,s.joining,nm.duty_type,s.address,s.`Ph.No.` from `Non-Medical Staff` as nm join staff as s using(s_id) where  s_id = '{StaffLogin.ids}';

select a.a_id,a.p_id,a.`date`,d.b_no,d.diagnosis,d.medicine,p.`date`,p.details from appointment as a join `procedure` as p using(a_id) join diagnosis as d using(a_id) where a.`status` = 'procedure' and p.r_no is null;

select r_no, r_type from room where status='free';

Select a.a_id, a.p_id,a.date, a.status, b.b_no From appointment as a Join billing as b using(a_id) Where a.a_id={NMSPage.aid} and (a.status ='diagnosis' or a.status ='procedure');

select b.diagnosis_cost, b.procedure_cost, b.medicine_cost,p.date,r.room_fee_per_day from billing as b join appointment as a using(a_id) left join `procedure` as p using(a_id) left join room as r using(r_no) where (a.status='procedure' or a.status='diagnosis') and a_id={NMSPage.aid};

Update billing Set diagnosis_cost = diagnosis_cost + {diagcost}, Medicine_cost = medicine_cost + {medcost}, Procedure_cost = procedure_cost + {procost}, Total_cost = procedure_cost + medicine_cost + diagnosis_cost Where a_id={NMSPage.aid};

select r_no from `procedure` where a_id={NMSPage.aid};

update billing as b join `procedure` as p using(a_id) join room as r using(r_no) set b.procedure_cost = b.procedure_cost + (current_date-p.date)*r.room_fee_per_day where b.a_id={NMSPage.aid};

Update billing Set diagnosis_cost = diagnosis_cost + {diagcost}, Medicine_cost = medicine_cost + {medcost}, Procedure_cost = procedure_cost + {procost}, Total_cost = procedure_cost + medicine_cost + diagnosis_cost Where a_id={NMSPage.aid};

update room as r join `procedure` as p using(r_no) set r.status='Free',r.nurse_1=null,r.nurse_2=null,p.r_no=null,p.date_discharge=current_date where p.a_id={NMSPage.aid};

update appointment set status='Completed' where a_id={NMSPage.aid};

select a.a_id from appointment as a join `procedure` as p using(a_id) join diagnosis as d using(a_id) where a.status = 'procedure' and p.r_no is null;

update `procedure` set r_no={room} where a_id = {aid};

update room set nurse_1=if('{nur1}' not like 'NUR%',null,'{nur1}'),nurse_2=if('{nur2}' not like 'NUR%',null,'{nur2}'), status='Occupied' where r_no={room};

Select s_id from nurse;