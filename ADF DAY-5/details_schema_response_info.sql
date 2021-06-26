-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: details_schema
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `response_info`
--

DROP TABLE IF EXISTS `response_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `response_info` (
  `response_id` int NOT NULL AUTO_INCREMENT,
  `request_id` int NOT NULL,
  `response_message` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`response_id`),
  KEY `request_id_idx` (`request_id`),
  CONSTRAINT `request_id` FOREIGN KEY (`request_id`) REFERENCES `request_info` (`id_num`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `response_info`
--

LOCK TABLES `response_info` WRITE;
/*!40000 ALTER TABLE `response_info` DISABLE KEYS */;
INSERT INTO `response_info` VALUES (1,6,'{\"6\": \"Eligible\"}'),(2,6,'{\"6\": \"Eligible\"}'),(3,11,'{\"11\": \"Eligible\"}'),(4,12,'{\"12\": \"Eligible\"}'),(5,13,'{\"13\": \"Eligible\"}'),(6,14,'{\"14\": \"Eligible\"}'),(7,15,'{\"15\": \"Eligible\"}'),(8,16,'{\"16\": \"Eligible\"}'),(9,22,'{\"22\": \"Not Eligible Not Eligible\"}'),(10,22,'{\"22\": \"Not Eligible Not Eligible\"}'),(11,22,'{\"22\": \"Eligible\"}'),(12,26,'{\"26\": \"Not Eligible Not Eligible\"}'),(13,26,'{\"26\": \"Not Eligible Not Eligible\"}'),(14,33,'{\"\'Request_id\':33\": \",\'Response\':\'Failed\',\'Reason\':\'Nationality does not match\'\"}'),(15,33,'{\"\'Request_id\':33\": \",\'Response\':\'Success\'\"}'),(16,34,'{\"\'Request_id\':34\": \",\'Response\':\'Failed\',\'Reason\':\'Salary is not within the range\'\"}'),(17,34,'{\"\'Request_id\':34\": \",\'Response\':\'Failed\',\'Reason\':\'Nationality does not match\'\"}'),(18,34,'{\"\'Request_id\':34\": \",\'Response\':\'Failed\',\'Reason\':\'State does not match\'\"}'),(19,34,'{\"\'Request_id\':34\": \",\'Response\':\'Success\'\"}'),(20,34,'{\"\'Request_id\':34\": \",\'Response\':\'Success\'\"}'),(21,36,'{\"\'Request_id\':36\": \",\'Response\':\'Success\'\"}'),(22,36,'{\"\'Request_id\':36\": \",\'Response\':\'Failed\',\'Reason\':\'Age is less than expected.\'\"}'),(23,2,'{\"\'Request_id\':2\": \",\'Response\':\'Success\'\"}'),(24,37,'{\"\'Request_id\':37\": \",\'Response\':\'Success\'\"}'),(25,38,'{\"\'Request_id\':38\": \",\'Response\':\'Success\'\"}'),(26,36,'{\"\'Request_id\':36\": \",\'Response\':\'Success\'\"}'),(27,3,'{\"\'Request_id\':3\": \",\'Response\':\'Success\'\"}'),(28,1,'{\"\'Request_id\':1\": \",\'Response\':\'Failed\',\'Reason\':\'Recently request received in last 5 days.\'\"}'),(29,38,'{\"\'Request_id\':38\": \",\'Response\':\'Success\'\"}'),(30,38,'{\"\'Request_id\':38\": \",\'Response\':\'Failed\',\'Reason\':\'Recently request received in last 5 days.\'\"}'),(31,1,'{\"\'Request_id\':1\": \",\'Response\':\'Success\'\"}'),(32,1,'{\"\'Request_id\':1\": \",\'Response\':\'Success\'\"}'),(33,39,'{\"\'Request_id\':39\": \",\'Response\':\'Failed\',\'Reason\':\'Recently request received in last 5 days.\'\"}'),(34,40,'{\"\'Request_id\':40\": \",\'Response\':\'Failed\',\'Reason\':\'Recently request received in last 5 days.\'\"}'),(35,41,'{\"\'Request_id\':41\": \",\'Response\':\'Failed\',\'Reason\':\'Recently request received in last 5 days.\'\"}'),(36,42,'{\"\'Request_id\':42\": \",\'Response\':\'Failed\',\'Reason\':\'Recently request received in last 5 days.\'\"}'),(37,1,'{\"\'Request_id\':1\": \",\'Response\':\'Success\'\"}'),(38,1,'{\"\'Request_id\':1\": \",\'Response\':\'Failed\',\'Reason\':\'Recently request received in last 5 days.\'\"}'),(39,1,'{\"\'Request_id\':1\": \",\'Response\':\'Success\'\"}');
/*!40000 ALTER TABLE `response_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-27  1:22:26
