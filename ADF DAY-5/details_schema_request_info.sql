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
-- Table structure for table `request_info`
--

DROP TABLE IF EXISTS `request_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request_info` (
  `id_num` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `middle_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `date_ofbirth` varchar(20) NOT NULL,
  `gender` varchar(8) NOT NULL,
  `nationality` varchar(45) NOT NULL,
  `current_city` varchar(45) DEFAULT NULL,
  `state` varchar(45) NOT NULL,
  `pin_code` int DEFAULT NULL,
  `qualification` varchar(45) DEFAULT NULL,
  `salary` int NOT NULL,
  `pan_number` varchar(25) NOT NULL,
  `request_date` date DEFAULT NULL,
  PRIMARY KEY (`id_num`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_info`
--

LOCK TABLES `request_info` WRITE;
/*!40000 ALTER TABLE `request_info` DISABLE KEYS */;
INSERT INTO `request_info` VALUES (1,'SOBIGHA','BALAKRISHNAN','B','2000-8-21','FEMALE','INDIAN','ERODE','TAMIL NADU',638301,'BE',50000,'tvxp89i','2021-06-27'),(2,'adithya','sanil','s','1997-8-3','male','indian','coonnor','tamil nadu',635412,'btech',50000,'TVXP56H','2021-06-26'),(3,'sobi','sobigha','balan','2000-8-17','female','indian','bhavani','tamil nadu',789654,'btech',20000,'TVCX562','2021-06-26'),(4,'adithyas','S','adityas','1996-8-21','male','indian','ooty','tamil nadu',698745,'BE',70000,'tvx564','2021-06-25'),(5,'Kishore','R','Radhakrishnan','1992-05-05','MALE','INDIAN','TIRUPPUR','TAMIL NADU',689412,'MBA',50000,'tvcx45','2021-06-25'),(6,'NIVI','NIVI','R H','2000-8-9','FEMALE','INDIAN','KARUR','TAMIL NADU',698745,'BE',40000,'PAN1','2021-06-26'),(8,'NIVI','NIVITHA ','SHREE','200-6-9','FEMALE','INDIAN','LOS ANGELS','KARNATAKA',632025,'BTECH',40000,'pan1','2021-06-26'),(9,'vasanth','t','','2000-8-23','male','indian','hosur','karnataka',632145,'BE',40000,'PAN1','2021-06-26'),(10,'Rakul','V','M','2001-5-6','MALE','INDIAN','CBE','TAMIL NADU',632145,'BE',40000,'123PANNUM','2021-06-26'),(11,'Rakul','V','M','2001-05-06','male','indian','cbe','TAMIL NADU',638301,'BE',40000,'PANNUMBER123','2021-06-26'),(12,'DELISH','KUMAR','R','2000-08-21','MALE','INDIAN','ERODE','KERALA',333666,'BE',40000,'#4563','2021-06-26'),(13,'DEEPAK','KUMAR','R','2000-08-25','MALE','RUSSIAN','EECF','ODISSA',12345,'BE',40000,'4%7897','2021-06-26'),(14,'delish','k','r','2002-08-05','male','indian','kerala','tamil nadu',630257,'BE',40000,'789098','2021-06-26'),(15,'GR','GV','VG','1993-8-27','MALE','RUSSIAN','ERF','KERALA',221,'BE',50000,'GVGHBHBJK','2021-06-26'),(16,'ffg','hbj','jbjn','2000-5-6','male','njknjn','hnjhj','njhnj',5566,'njn',50000,'jnuyt','2021-06-26'),(17,'bhk',' h',' h ','2000-5-20','yh','hjj','j','j',55,'j',20000,'uy','2021-06-26'),(18,'hbjh','nmj','nj','2000-8-5','jhb',' jh','h','j',2,'nioi',50000,'nui','2021-06-26'),(19,'hvg','jbhb','hjb','2000-8-17','jh','j','j','k',1,'h',50000,'nj','2021-06-26'),(20,'fv','fv','fv','2000-8-17','frf','f','f','fr',5,'fec',50000,'efcd','2021-06-26'),(21,'fcr','rd','d','2000-8-17','ed','de','de','de',5,'ed',50000,'deww','2021-06-26'),(22,'rtg','brg','rtg','2000-8-17','female','indadefw','rfert','gtr',30,'rr',200,'PANNUm','2021-06-26'),(23,'rbgbt','fbvrgb','fbrgn','2000-3-6','female','indian','evr','tamil nadu',200,'rf',5000,'PANNUmnbn','2021-06-26'),(24,'n','m','k','2000-8-17','male','indian','nnh','tamil nadu',2,'btech',300,'PANNUm','2021-06-26'),(25,'jb','l','m','2000-8-17','female','indian','kl','tamil nadu',31,'be',20000,'PANNUm','2021-06-26'),(26,'surya','suryaa','t','1993-8-6','male','indian','erode','andhra pradesh',222,'btec',20000,'ghjk','2021-06-26'),(27,'apple','berry','cherry','200-3-6','female','russian','weod','cefv',2,'rvr',200,'vvv','2021-06-26'),(28,'apple','apple','aooke','2000-9-6','female','rgrt','etgr','br',3,'vtr',2000,'vtr','2021-06-26'),(29,'vt','vfr','fv','2000-6-5','female','vr','vrf','vfr',0,'evrf',200,'gaaaa','2021-06-26'),(30,'goa','cherry','mango','2000-8-5','female','indina','ervt','tr',5,'er',2,'njm','2021-06-26'),(31,'bb',' bb','hb','2000-8-5','m','m','l','j',0,'k',2,'m','2021-06-26'),(32,'n','m','l','2000-8-5','m','b','h','j',0,'j',1,'v','2021-06-26'),(33,'sobigha','','balakrishnan','2000-8-17','female','indian','chennai','tamil nadu',654123,'be',80000,'cxc','2021-06-26'),(34,'SOBIGHA','B','BALAN','2000-8-17','FEMALE','INDIAN','ERODE','TAMIL NADU',6638301,'BE',80000,'ghjf','2021-06-26'),(35,'Sobigha','B','Balan','2000-8-17','female','indian','erode','tamil nadu',638301,'BE',80000,'T345','2021-06-26'),(36,'sobigha','balan','g','2000-8-17','female','american','mysore','tamil nadu',20048,'be',80000,'adi123','2021-06-26'),(37,'sobigha','balan','gurusamy','2000-8-17','female','indian','trichy','tamil nadu',638301,'btech',50000,'sobi123','2021-06-26'),(38,'sobigha','balan','gurusamy','2000-08-17','female','indian','erode','tamil nadu',638301,'be',20000,'asdfg','2021-06-18'),(39,'adi','m','s','1997-6-5','male','indian','erode','tamil nadu',456987,'be',20000,'werrf','2021-06-26'),(40,'werrf','fc','cf','1997-8-23','male','fedc','cf','fc',1,'cef',10000,'dfgg','2021-06-26'),(41,'soni','soniya','s','2000-8-17','female','indian','erode','tamil nadu',638301,'be',20000,'pan12578','2021-06-26'),(42,'sobigha','balakrishnan','gurusamy','2000-8-17','female','indian','erode','tamil nadu',638301,'BE',50000,'PAN1234','2021-06-27');
/*!40000 ALTER TABLE `request_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-27  1:22:25
