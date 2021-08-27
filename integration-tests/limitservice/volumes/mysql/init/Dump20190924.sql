-- MySQL dump 10.13  Distrib 8.0.17, for macos10.14 (x86_64)
--
-- Host: localhost    Database: anchorfree
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `active_session`
--

DROP TABLE IF EXISTS `active_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `active_session` (
  `id` varchar(255) NOT NULL,
  `credentials_id` bigint(20) DEFAULT NULL,
  `internal_ip` varchar(255) DEFAULT NULL,
  `protocol` varchar(255) DEFAULT NULL,
  `remote_ip` varchar(255) DEFAULT NULL,
  `time` bigint(20) DEFAULT NULL,
  `traffic` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `device_id` bigint(20) DEFAULT NULL,
  `rx` bigint(20) DEFAULT NULL,
  `server_id` bigint(20) DEFAULT NULL,
  `start_time` bigint(20) DEFAULT NULL,
  `tx` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `active_session_user_id_idx` (`user_id`),
  KEY `active_session_server_time_idx` (`server_id`,`time`),
  KEY `active_session_credentials_id_idx` (`credentials_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `active_session`
--

/*!40000 ALTER TABLE `active_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `active_session` ENABLE KEYS */;

--
-- Table structure for table `carrier`
--

DROP TABLE IF EXISTS `carrier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrier` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `identity` varchar(255) DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `project_type` varchar(255) DEFAULT NULL,
  `auth_version` bigint(2) DEFAULT NULL,
  `purchase_version` bigint(2) DEFAULT NULL,
  `traffic_limit_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `geo_mapping_template` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `config` mediumtext,
  `enabled` tinyint(1) NOT NULL DEFAULT '1',
  `reset` varchar(255) DEFAULT NULL,
  `description` varchar(4096) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `carrier_identity` (`identity`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrier`
--

/*!40000 ALTER TABLE `carrier` DISABLE KEYS */;
INSERT INTO `carrier` VALUES (1,'kasperskylab','KasperskyLab','public_vpn',2,2,'by_user','kl','{\"icon\":\"https://storage.googleapis.com/af-stage/project/kasperskylab/icon\",\"default_traffic_limit\":209715200,\"server_pool\":\"pub-kl\",\"server_group\":\"kasperskylab\",\"disable_optimal_location\":false}',1,'daily-utc','TouchVPN- iOS (IPSec, Hydra); ↵Android (OpenVPN, Hydra);↵Windows Store (IPSec);↵macOS (Hydra)'),(3,'touchvpn','TouchVPN','public_vpn',2,2,'by_user','default','{\"icon\":\"https://storage.googleapis.com/af-stage/project/touchvpn/icon\",\"application\":{\"macos\":{\"support\":[\"n.cherkashin@anhorfree.com\"]}},\"sd\":{\"android\":{\"sd\":{\"routes\":{\"torrent\":{\"sections\":[{\"servers\":[{\"ips\":[\"167.99.249.242\"]}]},{\"servers\":[{\"ips\":[\"167.99.245.18\"]}]},{\"servers\":[{\"ips\":[\"167.99.249.243\"]}]},{\"servers\":[{\"ips\":[\"162.243.36.54\"]}]},{\"servers\":[{\"ips\":[\"162.243.32.93\"]}]},{\"servers\":[{\"ips\":[\"162.243.28.103\"]}]},{\"servers\":[{\"ips\":[\"167.99.245.13\"]}]},{\"servers\":[{\"ips\":[\"62.243.33.179\"]}]},{\"servers\":[{\"ips\":[\"167.99.139.103\"]}]},{\"servers\":[{\"ips\":[\"162.243.33.153\"]}]}]}}}},\"windows\":{\"sd\":{\"routes\":{\"torrent\":{\"sections\":[{\"servers\":[{\"ips\":[\"167.99.249.242\"]}]},{\"servers\":[{\"ips\":[\"167.99.245.18\"]}]},{\"servers\":[{\"ips\":[\"167.99.249.243\"]}]},{\"servers\":[{\"ips\":[\"162.243.36.54\"]}]},{\"servers\":[{\"ips\":[\"162.243.32.93\"]}]},{\"servers\":[{\"ips\":[\"162.243.28.103\"]}]},{\"servers\":[{\"ips\":[\"167.99.245.13\"]}]},{\"servers\":[{\"ips\":[\"62.243.33.179\"]}]},{\"servers\":[{\"ips\":[\"167.99.139.103\"]}]},{\"servers\":[{\"ips\":[\"162.243.33.153\"]}]}]}}}}},\"files\":{\"test\":\"https://storage.googleapis.com/af-prod/project/touchvpn/files/test/e25fd8745d153bf8b7de5407147282482687fdfb\",\"bpl\":\"1a420b6f34466fc14bd88a814e9b31f153856d11\",\"cnl\":\"f97af29236bd332f175bda37dc92d1f4fc29b31c\"},\"server_pool\":\"pub-default\",\"server_group\":\"touchvpn\",\"private_pools\":[\"touchvpn-test-pool_1559922194486\",\"touchvpn-test-pool_1559922194486_1559922757429\",\"touchvpn-test-pool\"],\"private_groups\":[\"testrule3\",\"testrule1\",\"testrule2\",\"us-server\"],\"disable_optimal_location\":false}',1,'daily-utc','test'),(5,'mcafee','mcafee','public_vpn',2,2,'by_user','mcafee_msc2','{\"icon\":\"https://storage.googleapis.com/af-prod/project/touchvpn/icon\",\"default_traffic_limit\":262144000,\"server_group\":\"mcafee\"}',1,'monthly','TouchVPN- iOS (IPSec, Hydra); ↵Android (OpenVPN, Hydra);↵Windows Store (IPSec);↵macOS (Hydra)'),(8,'bizone_sm','test project.','public_vpn',2,2,'by_user','default','{\"server_pool\":\"pub-default\",\"disable_optimal_location\":false}',1,'daily-tz',NULL),(10,'mcafee_vz','Verizon','public_vpn',2,2,'by_user','mcafee','{\"allow_login_for_blocked_users\":true,\"disable_optimal_location\":false}',1,'monthly',NULL),(67,'bitdefender','bitdefender','public_vpn',2,2,'by_device','default','{\"icon\":\"https://storage.googleapis.com/af-prod/project/bitdefender/icon\",\"default_traffic_limit\":209715200,\"sd\":{\"android\":{\"modules\":{\"viper\":{\"generic-proxy\":{\"plugin-chain\":[{\"name\":\"vpr-rules\",\"id\":1,\"alert-page\":{\"domain\":\"connect.bitdefender.net\",\"path\":\"safe_zone.html\"}}]},\"categorization\":{\"service-enabled\":1,\"services\":[\"sophos\",\"bitdefender\",\"ip\"],\"alertpage_server\":\"%IP%:8000\",\"whitelist-size\":10000,\"categ-cache-size\":1000,\"categ-cache-timeout\":30,\"categ-request-timeout\":3000}}}},\"ios\":{\"modules\":{\"viper\":{\"generic-proxy\":{\"plugin-chain\":[{\"name\":\"vpr-rules\",\"alert-page\":{\"domain\":\"connect.bitdefender.net\",\"path\":\"safe_zone.html\"}}]},\"categorization\":{\"service-enabled\":1,\"services\":[\"sophos\",\"bitdefender\",\"ip\"],\"alertpage_server\":\"%IP%:8000\",\"whitelist-size\":10000,\"categ-cache-size\":1000,\"categ-cache-timeout\":30,\"categ-request-timeout\":3000}}}}},\"server_pool\":\"pub-default\",\"disable_optimal_location\":false,\"platform\":{\"android\":{\"ignoreLimits\":true}}}',1,'daily-utc',NULL),(97,'vpnintouch','vpnintouch','public_vpn',2,2,'by_user','default','{\"default_traffic_limit\":52428800,\"server_pool\":\"pub-default\",\"disable_optimal_location\":false}',1,'daily-utc',NULL);
/*!40000 ALTER TABLE `carrier` ENABLE KEYS */;

--
-- Table structure for table `carrier_admin`
--

DROP TABLE IF EXISTS `carrier_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrier_admin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `login` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `carrier_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_bkei5ny1dvvl4umq5gdpi73n3` (`carrier_id`),
  CONSTRAINT `FK_bkei5ny1dvvl4umq5gdpi73n3` FOREIGN KEY (`carrier_id`) REFERENCES `carrier` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrier_admin`
--

/*!40000 ALTER TABLE `carrier_admin` DISABLE KEYS */;
INSERT INTO `carrier_admin` VALUES (1,'kasperskylab','ieVaizei1Aim',1),(4,'mcafee_vz','Vpp2OE0MHI',10),(16,'touchvpn','bdgtY735nGde',3),(67,'bitdefender','sie3tha8Equi6iep',67),(97,'vpnintouch','uvf2tBKBO7',97);
/*!40000 ALTER TABLE `carrier_admin` ENABLE KEYS */;

--
-- Table structure for table `carrier_admin_firebase_uid`
--

DROP TABLE IF EXISTS `carrier_admin_firebase_uid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrier_admin_firebase_uid` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `carrier_id` bigint(20) DEFAULT NULL,
  `firebase_uid` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `carrier_admin_role_id` bigint(20) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `FK_carrier_admin_firebase_uid` (`carrier_id`),
  KEY `carrier_admin_role_id` (`carrier_admin_role_id`),
  CONSTRAINT `FK_carrier_admin_firebase_uid` FOREIGN KEY (`carrier_id`) REFERENCES `carrier` (`id`),
  CONSTRAINT `carrier_admin_firebase_uid_ibfk_1` FOREIGN KEY (`carrier_admin_role_id`) REFERENCES `carrier_admin_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrier_admin_firebase_uid`
--

/*!40000 ALTER TABLE `carrier_admin_firebase_uid` DISABLE KEYS */;
INSERT INTO `carrier_admin_firebase_uid` VALUES (1,1,'9pvBy1KH0ydTrwXYkW7vB9IIzgs1','alexey@anchorfree.com',1),(2,3,'9pvBy1KH0ydTrwXYkW7vB9IIzgs1','alexey@anchorfree.com',1),(3,10,'9pvBy1KH0ydTrwXYkW7vB9IIzgs1','alexey@anchorfree.com',1);
/*!40000 ALTER TABLE `carrier_admin_firebase_uid` ENABLE KEYS */;

--
-- Table structure for table `carrier_country`
--

DROP TABLE IF EXISTS `carrier_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrier_country` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `country` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `carrier_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_carrier_country_carrier` (`carrier_id`),
  CONSTRAINT `FK_carrier_country_carrier_id` FOREIGN KEY (`carrier_id`) REFERENCES `carrier` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2119 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrier_country`
--

/*!40000 ALTER TABLE `carrier_country` DISABLE KEYS */;
INSERT INTO `carrier_country` VALUES (79,'ru',1),(83,'de',67),(86,'de',5),(87,'ru',5),(88,'fr',5),(91,'ru',3),(92,'fr',3),(93,'us',3),(96,'us',67),(97,'de',7),(98,'us',7),(99,'de',2),(100,'ru',2),(101,'fr',2),(103,'de',2),(104,'ru',2),(105,'fr',2),(106,'us',2),(107,'de',6),(108,'ru',6),(109,'fr',6),(110,'us',6),(132,'demo',10),(136,'us',97),(137,'nl',97),(140,'nl',3),(141,'nl',67),(157,'us',10),(158,'nl',10),(159,'fr',10),(164,'nl',5),(211,'jp',3),(277,'us-east',5),(278,'us-west',5),(281,'us-east',10),(282,'us-west',10),(311,'ams',3),(508,'ny',3),(651,'tr',3),(661,'de',97),(2010,'jp',97),(2016,'de',3),(2017,'fr',97),(2018,'zu',1),(2086,'de',1),(2087,'fr',1),(2088,'us',1),(2089,'nl',1),(2118,'zw',1);
/*!40000 ALTER TABLE `carrier_country` ENABLE KEYS */;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `access_token` varchar(255) DEFAULT NULL,
  `active` bit(1) DEFAULT NULL,
  `device_id` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `register_time` datetime DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `device_device_id` (`device_id`),
  UNIQUE KEY `device_access_token` (`access_token`),
  KEY `FK_s9ldpb0w8p735xk2hkbgrhdol` (`user_id`),
  CONSTRAINT `FK_s9ldpb0w8p735xk2hkbgrhdol` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES (1,'nitmcrtsev77kh99tai8i5cisl9qtli64a3h19h3kij1mjrub8d',_binary '','5ebb4c0a98b0d1c9','Huawei Nexus 6P','2019-08-29 01:11:16','mobile',1001),(2,'17l7bpqnlaicvbualb09fi257dhbmtv8v4ftiq4n7aj2drcqmj74',_binary '','11112222444466667','iPhone10','2019-08-29 01:11:16','iOS',1002),(3,'1en6ddc8bomg7l0d8cqpanloi2141hrq27fm48eutsvo7lh27uo6',_binary '','lxrycuouykhgcj4677==','Samsung10','2019-08-29 01:11:16','android',1003),(4,'3fd6b5c8tpr2ra8i7bf9mp5j6djemkeo0cfrq9rc59rod03pamv',_binary '','005056C00001','DESKTOP-MFJO99G','2019-08-29 01:11:16','windows',1004),(5,'a8kjad1n3s7nndalr25ngg89adnlgfonge8rnmorbl5j4ofrnvi',_binary '','9a666555-bc4c-4d7e-5f64-e01567c05c6e','lozhkarev-w10','2019-08-29 01:11:16','desktop',1005);
/*!40000 ALTER TABLE `device` ENABLE KEYS */;

--
-- Table structure for table `license`
--

DROP TABLE IF EXISTS `license`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `license` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `devices` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `sessions` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `license`
--

/*!40000 ALTER TABLE `license` DISABLE KEYS */;
INSERT INTO `license` VALUES (1,1000,'default',1000),(2,1,'anonymus',1),(6,1,'1-1',1),(7,2,'2-2',2),(8,3,'3-3',3),(9,4,'4-4',4),(10,5,'5-5',5);
/*!40000 ALTER TABLE `license` ENABLE KEYS */;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session` (
  `id` varchar(255) NOT NULL,
  `carrier` varchar(255) DEFAULT NULL,
  `device_id` bigint(20) DEFAULT NULL,
  `end_time` bigint(20) DEFAULT NULL,
  `rx` bigint(20) DEFAULT NULL,
  `start_time` bigint(20) DEFAULT NULL,
  `tx` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `session_end_time_idx` (`end_time`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

/*!40000 ALTER TABLE `session` DISABLE KEYS */;
/*!40000 ALTER TABLE `session` ENABLE KEYS */;

--
-- Table structure for table `stat_time_report`
--

DROP TABLE IF EXISTS `stat_time_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stat_time_report` (
  `last_time_report` bigint(20) DEFAULT NULL,
  `report` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stat_time_report`
--

/*!40000 ALTER TABLE `stat_time_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `stat_time_report` ENABLE KEYS */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `condition_state` int(11) DEFAULT NULL,
  `extra` mediumtext CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `extref` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `family_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `given_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `locale` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `register_date` datetime DEFAULT NULL,
  `social_profiles` mediumtext CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `sub` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `traffic_limit` bigint(20) DEFAULT NULL,
  `traffic_start` bigint(20) DEFAULT NULL,
  `user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `carrier_id` bigint(20) DEFAULT NULL,
  `license_id` bigint(20) DEFAULT NULL,
  `traffic_used` bigint(20) DEFAULT NULL,
  `auth_method` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_username_carrier_idx` (`user_name`,`carrier_id`),
  KEY `FK_aboyh2m6a2eewkvrm9xmy449k` (`carrier_id`),
  KEY `FK_5bv6qtdr8fj4t0o43c5l6jbsb` (`license_id`),
  CONSTRAINT `FK_5bv6qtdr8fj4t0o43c5l6jbsb` FOREIGN KEY (`license_id`) REFERENCES `license` (`id`),
  CONSTRAINT `FK_aboyh2m6a2eewkvrm9xmy449k` FOREIGN KEY (`carrier_id`) REFERENCES `carrier` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,0,'{\"country\":\"EG\"}',NULL,'Doe','John',NULL,'2016-03-05 01:11:16','{\"github\":{\"id\":33,\"login\":\"ewrqso\",\"email\":\"wer@gmail.com\"}}',NULL,209715200,1567043207000,'anonymous_1660413481964131971',1,1,0,'anonymous'),(2,0,'{\"country\":\"EG\"}',NULL,'Doe','John',NULL,'2016-03-05 01:11:16','{\"github\":{\"id\":30,\"login\":\"ewrqso\",\"email\":\"wer@gmail.com\"}}',NULL,209715200,1567043207000,'anonymous_1660413481964131972',97,2,0,'anonymous'),(3,0,'{\"country\":\"EG\"}',NULL,'Doe','John',NULL,'2016-03-05 01:11:16','{\"github\":{\"id\":31,\"login\":\"ewrqso\",\"email\":\"wer@gmail.com\"}}',NULL,109715200,1567043207000,'anonymous_1660413481964131973',3,3,0,'anonymous'),(4,1,'{\"country\":\"RU\",\"language\":\"ru\"}',NULL,'Doe','John',NULL,'2016-03-05 01:11:16','{\"github\":{\"id\":32,\"login\":\"ewrqso\",\"email\":\"wer@gmail.com\"}}',NULL,59715200,1567043207000,'anonymous_1660413481964131974',10,5,0,'anonymous'),(5,1,'{\"country\":\"RU\",\"language\":\"ru\"}',NULL,'Doe','John',NULL,'2016-03-05 01:11:16','{\"github\":{\"id\":34,\"login\":\"ewrqso\",\"email\":\"wer@gmail.com\"}}',NULL,192837,1567043207000,'anonymous_1660413481964131975',67,6,0,'anonymous'),(6,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

--
-- Table structure for table `user_policy`
--

DROP TABLE IF EXISTS `user_policy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_policy` (
  `user_id` bigint(20) NOT NULL,
  `version` bigint(20) NOT NULL,
  `content` blob NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_policy`
--

/*!40000 ALTER TABLE `user_policy` DISABLE KEYS */;
INSERT INTO `user_policy` VALUES (1001,1,_binary '\"kasperskylab('),(1002,2,'');
/*!40000 ALTER TABLE `user_policy` ENABLE KEYS */;

--
-- Table structure for table `user_traffic`
--

DROP TABLE IF EXISTS `user_traffic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_traffic` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) DEFAULT NULL,
  `device_id` bigint(20) DEFAULT NULL,
  `traffic_limit` bigint(20) DEFAULT NULL,
  `traffic_start` bigint(20) DEFAULT NULL,
  `traffic_used` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_traffic_user_device_idx` (`user_id`,`device_id`),
  KEY `FK_user_traffic_device` (`device_id`),
  CONSTRAINT `FK_user_traffic_device` FOREIGN KEY (`device_id`) REFERENCES `device` (`id`),
  CONSTRAINT `FK_user_traffic_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_traffic`
--

/*!40000 ALTER TABLE `user_traffic` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_traffic` ENABLE KEYS */;

--
-- Table structure for table `vpn_client_credentials`
--

DROP TABLE IF EXISTS `vpn_client_credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vpn_client_credentials` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create_time` bigint(20) DEFAULT NULL,
  `expire_time` bigint(20) DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `device_id` bigint(20) DEFAULT NULL,
  `vpn_server_id` bigint(20) DEFAULT NULL,
  `issued_certificate_id` bigint(20) DEFAULT NULL,
  `connect` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cred_username_idx` (`username`) USING BTREE,
  KEY `FK_b37fer9cl2l2qvxngjmx66fa2` (`device_id`),
  KEY `FK_1q1cb23hyt9um05gy5s2plo4x` (`vpn_server_id`),
  KEY `FK_qdsyose0uc1cnlaygv94urle6` (`issued_certificate_id`),
  KEY `vpn_client_credentials_expire_time_idx` (`expire_time`),
  KEY `vpn_client_credentials_create_time_idx` (`create_time`),
  CONSTRAINT `FK_1q1cb23hyt9um05gy5s2plo4x` FOREIGN KEY (`vpn_server_id`) REFERENCES `vpn_server` (`id`),
  CONSTRAINT `FK_b37fer9cl2l2qvxngjmx66fa2` FOREIGN KEY (`device_id`) REFERENCES `device` (`id`),
  CONSTRAINT `FK_qdsyose0uc1cnlaygv94urle6` FOREIGN KEY (`issued_certificate_id`) REFERENCES `issued_certificate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vpn_client_credentials`
--

/*!40000 ALTER TABLE `vpn_client_credentials` DISABLE KEYS */;
/*!40000 ALTER TABLE `vpn_client_credentials` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed
