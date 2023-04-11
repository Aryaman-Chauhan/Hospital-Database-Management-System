CREATE DATABASE IF NOT EXISTS Hospital;
USE Hospital;

CREATE TABLE `Diagnosis`(
    `a_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `b_no` INT UNSIGNED NOT NULL,
    `Diagnosis` VARCHAR(500) NOT NULL DEFAULT '',
    `Medicine` VARCHAR(500) NOT NULL DEFAULT '',
    PRIMARY KEY(`a_id`)
);

CREATE TABLE `Room`(
    `r_no` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `r_type` VARCHAR(10) DEFAULT 'GENERAL' NOT NULL CONSTRAINT CHECK(r_type IN("VIP", "General", "Children", "Public")),
    `room_fee_per_day` DECIMAL(8, 2) NOT NULL,
    `nurse_1` VARCHAR(8) NULL,
    `nurse_2` VARCHAR(8) NULL,
    `status` VARCHAR(8) DEFAULT 'Free' NOT NULL CONSTRAINT CHECK(`status` in ('Free','Occupied')),
    PRIMARY KEY(`r_no`)
);

CREATE TABLE `Doctor`(
    `s_id` VARCHAR(8) NOT NULL,
    `dep_id` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `Doctor` ADD PRIMARY KEY(`s_id`);
CREATE TABLE `Staff`(
    `s_id` VARCHAR(8) NOT NULL,
    `s_name` VARCHAR(255) NOT NULL,
    `salary` DECIMAL(8, 2) NOT NULL,
    `retirement` DATE,
    `gender` VARCHAR(10) NOT NULL,
    `password` VARCHAR(20) DEFAULT '0000',
    `joining` DATE NOT NULL,
    `Ph.No.` VARCHAR(10) NOT NULL,
    `Address` VARCHAR(200) NOT NULL
);
ALTER TABLE
    `Staff` ADD PRIMARY KEY(`s_id`);
CREATE TABLE `Departments`(
    `dep_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `Dep_name` VARCHAR(20) NOT NULL,
    PRIMARY KEY(`dep_id`)
);
CREATE TABLE `Nurse`(
    `s_id` VARCHAR(8) NOT NULL,
    `seniority` VARCHAR(255) NOT NULL,
    `dep_id` INT UNSIGNED NOT NULL
);
ALTER TABLE
    `Nurse` ADD PRIMARY KEY(`s_id`);
CREATE TABLE `Patient`(
    `p_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `p_name` VARCHAR(255) NOT NULL,
    `gender` VARCHAR(10) NOT NULL,
    `Address` VARCHAR(200) NOT NULL,
    `Ph.No.` VARCHAR(10) NOT NULL,
    `password` VARCHAR(20) NOT NULL DEFAULT '0000',
    PRIMARY KEY(`p_id`)
);

CREATE TABLE `Appointment`(
    `a_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `p_id` INT UNSIGNED NOT NULL,
    `s_id` VARCHAR(8) NOT NULL,
    `date` DATE NOT NULL,
    `Status` VARCHAR(20) DEFAULT 'pending' CONSTRAINT CHECK(STATUS IN('pending', 'cancelled', 'procedure', 'diagnosis', 'completed')),
    PRIMARY KEY(`a_id`)
);

CREATE TABLE `Procedure`(
    `a_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `date` DATE NOT NULL,
    `r_no` INT UNSIGNED NULL,
    `date_discharge` DATE NULL,
    `details` VARCHAR(500) NOT NULL DEFAULT '',
    PRIMARY KEY(`a_id`, `date`)
);

CREATE TABLE `Billing`(
    `b_no` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `p_id` INT UNSIGNED NOT NULL,
    `date` DATE NOT NULL,
    `diagnosis_cost` DECIMAL(8, 2) NOT NULL DEFAULT 0,
    `a_id` INT UNSIGNED NULL,
    `medicine_cost` DECIMAL(8, 2) NOT NULL DEFAULT 0,
    `procedure_cost` DECIMAL(8, 2) NOT NULL DEFAULT 0,
    `total_cost` DECIMAL(8, 2) NOT NULL DEFAULT 0,
    PRIMARY KEY(`b_no`)
);

CREATE TABLE `Non-Medical Staff`(
    `s_id` VARCHAR(8) NOT NULL,
    `duty_type` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Non-Medical Staff` ADD PRIMARY KEY(`s_id`);
ALTER TABLE
    `Procedure` ADD CONSTRAINT `procedure_r_no_foreign` FOREIGN KEY(`r_no`) REFERENCES `Room`(`r_no`);
ALTER TABLE
    `Appointment` ADD CONSTRAINT `appointment_s_id_foreign` FOREIGN KEY(`s_id`) REFERENCES `Doctor`(`s_id`);
ALTER TABLE
    `Appointment` ADD CONSTRAINT `appointment_p_id_foreign` FOREIGN KEY(`p_id`) REFERENCES `Patient`(`p_id`);
ALTER TABLE
    `Diagnosis` ADD CONSTRAINT `diagnosis_b_no_foreign` FOREIGN KEY(`b_no`) REFERENCES `Billing`(`b_no`);
ALTER TABLE
    `Appointment` ADD CONSTRAINT `appointment_a_id_foreign` FOREIGN KEY(`a_id`) REFERENCES `Procedure`(`a_id`);
ALTER TABLE
    `Doctor` ADD CONSTRAINT `doctor_dep_id_foreign` FOREIGN KEY(`dep_id`) REFERENCES `Departments`(`dep_id`);
ALTER TABLE
    `Nurse` ADD CONSTRAINT `nurse_dep_id_foreign` FOREIGN KEY(`dep_id`) REFERENCES `Departments`(`dep_id`);
ALTER TABLE
    `Appointment` ADD CONSTRAINT `appointment_a_id_foreign1` FOREIGN KEY(`a_id`) REFERENCES `Diagnosis`(`a_id`);
ALTER TABLE
    `Nurse` ADD CONSTRAINT `nurse_s_id_foreign` FOREIGN KEY(`s_id`) REFERENCES `Staff`(`s_id`);
ALTER TABLE
    `Non-Medical Staff` ADD CONSTRAINT `non_medical staff_s_id_foreign` FOREIGN KEY(`s_id`) REFERENCES `Staff`(`s_id`);
ALTER TABLE
    `Billing` ADD CONSTRAINT `billing_p_id_foreign` FOREIGN KEY(`p_id`) REFERENCES `Patient`(`p_id`);
ALTER TABLE
    `Room` ADD CONSTRAINT `room_nurse_1_foreign` FOREIGN KEY(`nurse_1`) REFERENCES `Nurse`(`s_id`);
ALTER TABLE
    `Doctor` ADD CONSTRAINT `doctor_s_id_foreign` FOREIGN KEY(`s_id`) REFERENCES `Staff`(`s_id`);