CREATE DATABASE  IF NOT EXISTS `hospital` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hospital`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `a_id` int unsigned NOT NULL AUTO_INCREMENT,
  `p_id` int unsigned NOT NULL,
  `s_id` varchar(8) NOT NULL,
  `date` date NOT NULL,
  `Status` varchar(20) DEFAULT 'pending',
  PRIMARY KEY (`a_id`),
  CONSTRAINT `appointment_chk_1` CHECK ((`STATUS` in (_utf8mb4'pending',_utf8mb4'procedure',_utf8mb4'diagnosis',_utf8mb4'completed',_utf8mb4'cancelled')))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `billing`
--

DROP TABLE IF EXISTS `billing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `billing` (
  `b_no` int unsigned NOT NULL AUTO_INCREMENT,
  `p_id` int unsigned NOT NULL,
  `date` date NOT NULL,
  `diagnosis_cost` decimal(8,2) NOT NULL DEFAULT '0.00',
  `a_id` int unsigned DEFAULT NULL,
  `medicine_cost` decimal(8,2) NOT NULL DEFAULT '0.00',
  `procedure_cost` decimal(8,2) NOT NULL DEFAULT '0.00',
  `total_cost` decimal(8,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`b_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billing`
--

LOCK TABLES `billing` WRITE;
/*!40000 ALTER TABLE `billing` DISABLE KEYS */;
/*!40000 ALTER TABLE `billing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `dep_id` int unsigned NOT NULL AUTO_INCREMENT,
  `Dep_name` varchar(20) NOT NULL,
  PRIMARY KEY (`dep_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Surgical'),(2,'Dietary'),(3,'Pediatric'),(4,'Radiology'),(5,'Cardiology'),(6,'Paramedical'),(7,'Neurology'),(8,'Gynaecology'),(9,'Dentistry');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnosis`
--

DROP TABLE IF EXISTS `diagnosis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagnosis` (
  `a_id` int unsigned NOT NULL AUTO_INCREMENT,
  `b_no` int unsigned NOT NULL,
  `Diagnosis` varchar(500) NOT NULL,
  `Medicine` varchar(500) NOT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnosis`
--

LOCK TABLES `diagnosis` WRITE;
/*!40000 ALTER TABLE `diagnosis` DISABLE KEYS */;
/*!40000 ALTER TABLE `diagnosis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `s_id` varchar(8) NOT NULL,
  `dep_id` int unsigned NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES ('DOC0000',1),('DOC0001',8),('DOC0002',7);
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `non-medical staff`
--

DROP TABLE IF EXISTS `non-medical staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `non-medical staff` (
  `s_id` varchar(8) NOT NULL,
  `duty_type` varchar(255) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `non-medical staff`
--

LOCK TABLES `non-medical staff` WRITE;
/*!40000 ALTER TABLE `non-medical staff` DISABLE KEYS */;
INSERT INTO `non-medical staff` VALUES ('DOC0000','admin'),('NMS0001','Cleaner'),('NMS0002','Reception');
/*!40000 ALTER TABLE `non-medical staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nurse`
--

DROP TABLE IF EXISTS `nurse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nurse` (
  `s_id` varchar(8) NOT NULL,
  `seniority` varchar(255) NOT NULL,
  `dep_id` int unsigned NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nurse`
--

LOCK TABLES `nurse` WRITE;
/*!40000 ALTER TABLE `nurse` DISABLE KEYS */;
INSERT INTO `nurse` VALUES ('DOC0000','admin',1),('NUR0001','Experienced',3),('NUR0002','Experienced',3);
/*!40000 ALTER TABLE `nurse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `p_id` int unsigned NOT NULL AUTO_INCREMENT,
  `p_name` varchar(255) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Ph.No.` varchar(10) NOT NULL,
  `password` varchar(20) NOT NULL DEFAULT '0000',
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,'Aryaman Chauhan','Male','Vyas Bhawan,\nBITS Pilani,\nPilani\n','9639226969','arya'),(2,'Devansh','Male','Vyas Bhawan,\nBITS Pilani,\nPilani\n','9077578789','dank');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `procedure`
--

DROP TABLE IF EXISTS `procedure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `procedure` (
  `a_id` int unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `r_no` int unsigned DEFAULT NULL,
  `date_discharge` date DEFAULT NULL,
  `details` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`a_id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `procedure`
--

LOCK TABLES `procedure` WRITE;
/*!40000 ALTER TABLE `procedure` DISABLE KEYS */;
/*!40000 ALTER TABLE `procedure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `r_no` int unsigned NOT NULL AUTO_INCREMENT,
  `r_type` varchar(10) NOT NULL,
  `room_fee_per_day` decimal(8,2) NOT NULL,
  `nurse_1` varchar(8) DEFAULT NULL,
  `nurse_2` varchar(8) DEFAULT NULL,
  `status` varchar(10) NOT NULL DEFAULT 'Free',
  PRIMARY KEY (`r_no`),
  CONSTRAINT `room_chk_1` CHECK ((`r_type` in (_utf8mb4'VIP',_utf8mb4'General',_utf8mb4'Children',_utf8mb4'Public'))),
  CONSTRAINT `room_stat` CHECK ((`status` in (_utf8mb4'Free',_utf8mb4'Occupied')))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (1,'VIP',1000.00,NULL,NULL,'Free');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `s_id` varchar(8) NOT NULL,
  `s_name` varchar(255) NOT NULL,
  `salary` decimal(8,2) NOT NULL,
  `retirement` date DEFAULT NULL,
  `password` varchar(20) DEFAULT '0000',
  `joining` date NOT NULL,
  `Ph.No.` varchar(10) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `gender` varchar(10) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES ('DOC0000','ADMIN',100000.00,NULL,'0000','2023-04-09','1234567890','Pilani hospital,pilani','Male'),('DOC0001','Tanisha Sharma',50000.00,NULL,'tasha','2023-04-10','9029484645','Meera Bhawan, BITS Pilani, Pilani','Female'),('DOC0002','Ranvir Kumar',60000.00,NULL,'raki','2023-04-10','9089589333','FD-III,\nBITS Pilani,\nPilani\n','Male'),('NMS0001','Ramu Kumar',13000.00,NULL,'ramu','2023-04-10','8967695487','Worker Quartes,\nPilani Campus,\nBITS Pilani,\nPilani\n','Male'),('NMS0002','John King',18000.00,NULL,'joking','2023-04-10','8964342487','FD-II\nPilani Campus,\nBITS Pilani,\nPilani\n','Male'),('NUR0001','Armaan Singh',18000.00,NULL,'arms','2023-04-09','9087754645','Station Road, Pilani','Male'),('NUR0002','Gretha Thumling',20000.00,NULL,'gret','2023-04-09','8976403210','Staff Quarters,\nBITS Pilani,\nPilani-333013\n','Female');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'hospital'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-11  0:04:45
