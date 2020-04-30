-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: mydatabase
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `e_category`
--

DROP TABLE IF EXISTS `e_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `e_category` (
  `expense_category_id` int(4) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`expense_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `e_category`
--

LOCK TABLES `e_category` WRITE;
/*!40000 ALTER TABLE `e_category` DISABLE KEYS */;
INSERT INTO `e_category` VALUES (1,'food'),(2,'bill'),(3,'travel'),(4,'stationery'),(5,'entertainment'),(6,'clothing'),(7,'tax'),(8,'health'),(9,'social'),(10,'education');
/*!40000 ALTER TABLE `e_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense`
--

DROP TABLE IF EXISTS `expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expense` (
  `expense_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL,
  `expense_category_id` int(11) NOT NULL,
  `expense_date` datetime NOT NULL,
  `amount` int(11) NOT NULL,
  `comments` varchar(2000) COLLATE utf8mb4_0900_as_cs DEFAULT NULL,
  PRIMARY KEY (`expense_id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense`
--

LOCK TABLES `expense` WRITE;
/*!40000 ALTER TABLE `expense` DISABLE KEYS */;
INSERT INTO `expense` VALUES (1,2,1,'2020-03-01 15:45:00',10000,'Grocery'),(2,1,4,'2020-03-02 13:00:00',500,'Notebooks'),(3,3,1,'2020-03-05 19:55:00',150,NULL),(4,2,4,'2020-03-07 13:00:00',50,NULL),(5,2,1,'2020-03-24 20:26:37',1000,NULL),(6,3,4,'2020-03-24 20:26:40',453,'Engineering Drawing material'),(7,3,4,'2020-04-24 20:26:40',3333,'Mobile'),(8,1,1,'2020-04-25 20:26:40',1000,'Food'),(9,1,1,'2020-04-25 20:26:40',122,NULL),(10,3,1,'2020-04-25 20:26:41',11,NULL),(11,1,6,'2020-04-25 20:26:42',22,'Clothes for Harry'),(12,3,4,'2020-04-25 20:27:40',222,NULL),(13,2,4,'2020-04-25 20:30:40',92992,'Red pens'),(14,3,1,'2020-04-25 20:45:40',22,NULL),(15,3,9,'2020-04-25 20:45:42',100,'Charity'),(16,1,1,'2020-04-27 13:33:28',1009,'Grocery'),(17,1,3,'2020-04-27 13:42:26',100,'Train'),(18,1,4,'2020-04-27 13:43:15',100,'Drawing Brush'),(19,1,5,'2020-04-27 13:46:20',1222,'Other'),(20,1,2,'2020-04-27 16:03:43',300,'Wi-fi bill'),(25,3,1,'2020-04-29 11:54:36',198,'No comments'),(26,3,4,'2020-04-29 11:56:15',2000,'Drawing Book'),(27,1,1,'2020-04-29 11:59:04',1,'none'),(28,2,3,'2020-04-29 12:15:20',1,'No comments'),(29,3,1,'2020-04-29 12:15:54',200,'BKC'),(30,1,5,'2020-04-29 12:17:04',250,'Blood test'),(31,1,1,'2020-04-29 12:18:36',2,'None'),(32,2,7,'2020-04-29 12:20:05',400,'Income Tax'),(33,1,1,'2020-04-29 12:20:23',34,'Mumbai'),(34,2,1,'2020-04-29 12:33:01',1222,'BMC'),(35,2,2,'2020-04-29 12:34:30',2222,'Hotel Bill'),(36,3,4,'2020-04-29 12:37:22',266,'None'),(37,2,1,'2020-04-29 12:38:20',111,'None'),(38,1,10,'2020-04-29 12:40:17',2000,'School Fees'),(39,2,8,'2020-04-29 12:43:42',220,'Dentist'),(40,3,3,'2020-04-29 23:07:00',5000,'Mumbai'),(41,2,4,'2020-04-29 23:12:48',200,'Black Pen'),(42,2,2,'2020-04-29 23:19:10',300,'Bill'),(43,1,4,'2020-04-29 23:20:46',34,'Pencil'),(44,1,3,'2020-04-30 12:35:34',999,'Pune');
/*!40000 ALTER TABLE `expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family`
--

DROP TABLE IF EXISTS `family`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) DEFAULT 'null',
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family`
--

LOCK TABLES `family` WRITE;
/*!40000 ALTER TABLE `family` DISABLE KEYS */;
INSERT INTO `family` VALUES (1,'Harry','Potter','TheChosenOne','Harry0912'),(2,'James','Potter','Prongs','James786'),(3,'Lily','Potter','HeadGirl','Lily7453');
/*!40000 ALTER TABLE `family` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `i_category`
--

DROP TABLE IF EXISTS `i_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `i_category` (
  `income_category_id` int(4) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`income_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `i_category`
--

LOCK TABLES `i_category` WRITE;
/*!40000 ALTER TABLE `i_category` DISABLE KEYS */;
INSERT INTO `i_category` VALUES (1,'salary'),(2,'prize'),(3,'rental'),(4,'dividends'),(5,'sale'),(6,'refunds'),(7,'investments'),(8,'others');
/*!40000 ALTER TABLE `i_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `income`
--

DROP TABLE IF EXISTS `income`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `income` (
  `income_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL,
  `income_category_id` int(11) NOT NULL,
  `income_date` datetime NOT NULL,
  `amount` int(11) NOT NULL,
  `comments` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`income_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `income`
--

LOCK TABLES `income` WRITE;
/*!40000 ALTER TABLE `income` DISABLE KEYS */;
INSERT INTO `income` VALUES (1,3,1,'2020-01-03 09:00:00',100000,'salary'),(2,3,2,'2020-10-03 01:00:00',20000,'prize'),(3,1,2,'2020-04-27 15:56:33',99999,'Instagram'),(4,2,3,'2020-04-27 15:59:11',12222,'Rent of vasai flat'),(5,3,4,'2020-04-27 16:01:48',12220,'No comments'),(6,1,1,'2020-04-27 16:03:08',99000,'Monthly salary'),(7,2,2,'2020-04-29 23:05:07',20000,'Prize'),(8,2,1,'2020-04-29 23:22:34',40000,'Bonus'),(9,1,4,'2020-04-30 12:36:16',10000,'None');
/*!40000 ALTER TABLE `income` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-30 13:04:35
