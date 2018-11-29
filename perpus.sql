/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 10.1.35-MariaDB : Database - perpustakaan
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`perpustakaan` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `perpustakaan`;

/*Table structure for table `buku` */

DROP TABLE IF EXISTS `buku`;

CREATE TABLE `buku` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_buku` varchar(30) DEFAULT NULL,
  `sinopsis` text,
  `id_pengarang` int(10) DEFAULT NULL,
  `id_penerbit` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_pengarang` (`id_pengarang`),
  KEY `id_penerbit` (`id_penerbit`),
  CONSTRAINT `buku_ibfk_1` FOREIGN KEY (`id_pengarang`) REFERENCES `pengarang` (`id`),
  CONSTRAINT `buku_ibfk_2` FOREIGN KEY (`id_penerbit`) REFERENCES `penerbit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `buku` */

insert  into `buku`(`id`,`nama_buku`,`sinopsis`,`id_pengarang`,`id_penerbit`) values 
(1,'java for dummies',NULL,1,1),
(2,'android for dummies',NULL,1,1),
(3,'tutorial laravel',NULL,1,1),
(4,'android exper',NULL,1,1),
(5,'create design for web',NULL,2,1),
(6,'optimize your SEO',NULL,2,1),
(7,'design web',NULL,2,1),
(8,'android beginner',NULL,3,2),
(9,'android beginner part 2',NULL,3,2),
(10,'exper on java part 3',NULL,3,2),
(11,'simple biology',NULL,4,3),
(12,'natural language processing',NULL,4,3),
(13,'information retrieval',NULL,5,4),
(14,'mixed reality',NULL,6,5);

/*Table structure for table `detail_buku` */

DROP TABLE IF EXISTS `detail_buku`;

CREATE TABLE `detail_buku` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_buku` int(10) DEFAULT NULL,
  `kode_barcode` varchar(30) DEFAULT NULL,
  `id_rak` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_buku` (`id_buku`),
  KEY `id_rak` (`id_rak`),
  CONSTRAINT `detail_buku_ibfk_1` FOREIGN KEY (`id_buku`) REFERENCES `buku` (`id`),
  CONSTRAINT `detail_buku_ibfk_2` FOREIGN KEY (`id_rak`) REFERENCES `rak` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `detail_buku` */

insert  into `detail_buku`(`id`,`id_buku`,`kode_barcode`,`id_rak`) values 
(1,1,'1283761287',1),
(2,1,'124313512',1),
(3,1,'1413513511',2),
(4,2,'23928922',3),
(5,2,'23892',3),
(6,3,'19028198',4),
(7,3,'18288172',1),
(8,3,'7812638172',2),
(9,4,'1y23781827',2),
(10,4,'16256711',4),
(11,5,'71273618237',1),
(12,6,'817289172',2),
(13,7,'17298172981',2),
(15,8,'172y1782',7),
(16,9,'182791872918',2),
(17,3,'671526712',1),
(18,5,'16521625',2),
(19,6,'61261711',2),
(20,7,'67123613',6),
(21,1,'1625716217',2);

/*Table structure for table `detail_pemesanan` */

DROP TABLE IF EXISTS `detail_pemesanan`;

CREATE TABLE `detail_pemesanan` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_pemesanan` int(10) DEFAULT NULL,
  `id_buku` int(10) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_pemesanan` (`id_pemesanan`),
  KEY `id_buku` (`id_buku`),
  CONSTRAINT `detail_pemesanan_ibfk_1` FOREIGN KEY (`id_pemesanan`) REFERENCES `pemesanan_buku` (`id`),
  CONSTRAINT `detail_pemesanan_ibfk_2` FOREIGN KEY (`id_buku`) REFERENCES `buku` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `detail_pemesanan` */

/*Table structure for table `detail_peminjaman` */

DROP TABLE IF EXISTS `detail_peminjaman`;

CREATE TABLE `detail_peminjaman` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_peminjaman` int(10) DEFAULT NULL,
  `id_detil_buku` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_peminjaman` (`id_peminjaman`),
  KEY `id_buku` (`id_detil_buku`),
  CONSTRAINT `detail_peminjaman_ibfk_1` FOREIGN KEY (`id_peminjaman`) REFERENCES `peminjaman` (`id`),
  CONSTRAINT `detail_peminjaman_ibfk_2` FOREIGN KEY (`id_detil_buku`) REFERENCES `detail_buku` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

/*Data for the table `detail_peminjaman` */

insert  into `detail_peminjaman`(`id`,`id_peminjaman`,`id_detil_buku`) values 
(1,1,1),
(2,1,4),
(3,2,1),
(4,2,2),
(5,3,3),
(6,3,4),
(7,4,5),
(8,4,6),
(9,5,7),
(10,5,8),
(11,6,9),
(12,6,10),
(13,6,1),
(14,7,4),
(15,8,2),
(16,9,2),
(18,10,5),
(19,11,2),
(20,11,5),
(21,12,8),
(22,13,1),
(23,14,8),
(24,15,11),
(25,15,10),
(26,16,2),
(27,17,8),
(29,18,16),
(30,18,1),
(31,18,3),
(32,18,5),
(33,19,8),
(34,19,7),
(35,20,1),
(36,20,2),
(37,20,3),
(38,21,1),
(39,21,6),
(40,21,3),
(41,22,1),
(42,22,2),
(44,23,10),
(45,23,18),
(46,24,6),
(47,25,7),
(48,25,8),
(49,25,1),
(50,26,7),
(51,26,19);

/*Table structure for table `member` */

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_member` varchar(30) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `telepon` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `member` */

insert  into `member`(`id`,`nama_member`,`jenis_kelamin`,`alamat`,`telepon`) values 
(1,'deva','Perempuan','badung','081234567890'),
(2,'agus','Laki-Laki','denpasar','08912612637'),
(3,'anang','Laki-Laki','jakarta','09826172722'),
(4,'budi','Laki-Laki','jimbaran','08976535412'),
(5,'budiman','Laki-Laki','klungkung','082746262626'),
(6,'raisa','Perempuan','badung','081726262626'),
(7,'andini','Perempuan','gianyar','08917162626'),
(8,'natasya','Perempuan','bangli','089171662762'),
(9,'anunya','Perempuan','singaraja','082616152628');

/*Table structure for table `pegawai` */

DROP TABLE IF EXISTS `pegawai`;

CREATE TABLE `pegawai` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_pegawai` varchar(30) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `telepon` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `pegawai` */

insert  into `pegawai`(`id`,`nama_pegawai`,`jenis_kelamin`,`alamat`,`telepon`) values 
(1,'devi','Perempuan','badung','081234567890'),
(2,'wowo','Laki-Laki','klungkung','082746262626'),
(3,'raisi','Perempuan','badung','081726262626'),
(4,'andina','Perempuan','gianyar','08917162626'),
(5,'natasa','Perempuan','bangli','089171662762'),
(6,'agung','Laki-Laki','denpasar','08912612637'),
(7,'hermansyah','Laki-Laki','jakarta','09826172722'),
(8,'budiwan','Laki-Laki','jimbaran','08976535412'),
(9,'itunya','Perempuan','singaraja','082616152628');

/*Table structure for table `pemesanan_buku` */

DROP TABLE IF EXISTS `pemesanan_buku`;

CREATE TABLE `pemesanan_buku` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_penerbit` int(10) DEFAULT NULL,
  `id_pegawai` int(10) DEFAULT NULL,
  `tanggal_sampai` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_penerbit` (`id_penerbit`),
  KEY `id_pegawai` (`id_pegawai`),
  CONSTRAINT `pemesanan_buku_ibfk_1` FOREIGN KEY (`id_penerbit`) REFERENCES `penerbit` (`id`),
  CONSTRAINT `pemesanan_buku_ibfk_2` FOREIGN KEY (`id_pegawai`) REFERENCES `pegawai` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `pemesanan_buku` */

/*Table structure for table `peminjaman` */

DROP TABLE IF EXISTS `peminjaman`;

CREATE TABLE `peminjaman` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_pegawai` int(10) DEFAULT NULL,
  `id_member` int(10) DEFAULT NULL,
  `tgl_pinjam` datetime DEFAULT NULL,
  `tgl_harus_kembali` datetime DEFAULT NULL,
  `tgl_kembali` datetime DEFAULT NULL,
  `denda` int(11) DEFAULT NULL,
  `status` enum('pinjam','selesai','jatuh tempo') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_pegawai` (`id_pegawai`),
  KEY `id_member` (`id_member`),
  CONSTRAINT `peminjaman_ibfk_1` FOREIGN KEY (`id_pegawai`) REFERENCES `pegawai` (`id`),
  CONSTRAINT `peminjaman_ibfk_2` FOREIGN KEY (`id_member`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;

/*Data for the table `peminjaman` */

insert  into `peminjaman`(`id`,`id_pegawai`,`id_member`,`tgl_pinjam`,`tgl_harus_kembali`,`tgl_kembali`,`denda`,`status`) values 
(1,1,1,'2018-11-17 21:43:34','2018-11-24 21:43:37',NULL,NULL,'pinjam'),
(2,1,2,'2018-01-01 14:20:39','2018-01-08 14:20:55','2018-01-07 14:25:56',NULL,'selesai'),
(3,1,3,'2018-01-02 14:21:25','2018-01-09 14:21:37','2018-01-08 14:26:16',NULL,'selesai'),
(4,2,4,'2018-01-03 14:24:50','2018-01-10 14:25:00','2018-01-09 14:26:29',NULL,'selesai'),
(5,2,5,'2018-01-04 14:26:47','2018-01-11 14:27:16','2018-01-10 14:27:35',NULL,'selesai'),
(6,2,6,'2018-01-05 14:28:03','2018-01-12 14:28:15','2018-01-11 14:29:08',NULL,'selesai'),
(7,3,7,'2018-01-06 14:29:29','2018-01-13 14:29:39','2018-01-12 14:29:50',NULL,'selesai'),
(8,2,8,'2018-01-07 14:30:12','2018-01-14 14:30:21','2018-01-13 14:30:37',NULL,'selesai'),
(9,3,9,'2018-01-08 14:30:59','2018-01-15 14:31:07','2018-01-14 14:31:18',NULL,'selesai'),
(10,4,1,'2018-02-01 14:35:22','2018-02-08 14:35:30','2018-02-07 14:35:38',NULL,'selesai'),
(11,4,3,'2018-02-05 14:35:59','2018-02-12 14:36:10','2018-02-11 14:36:19',NULL,'selesai'),
(12,4,5,'2018-02-13 14:36:42','2018-02-20 14:36:53','2018-02-19 14:37:01',NULL,'selesai'),
(13,4,1,'2018-02-10 14:37:45','2018-02-17 14:37:57','2018-02-16 14:38:06',NULL,'selesai'),
(14,4,1,'2018-02-19 14:38:31','2018-02-26 14:38:46','2018-02-25 14:38:56',NULL,'selesai'),
(15,5,2,'2018-03-05 14:39:16','2018-03-12 14:39:26','2018-03-11 14:39:35',NULL,'selesai'),
(16,5,4,'2018-03-07 14:40:11','2018-03-14 14:40:24','2018-03-13 14:40:32',NULL,'selesai'),
(17,5,9,'2018-03-15 14:40:50','2018-03-22 14:40:58','2018-03-21 14:41:08',NULL,'selesai'),
(18,5,4,'2018-03-22 14:41:26','2018-03-29 14:41:36','2018-03-28 14:41:46',NULL,'selesai'),
(19,1,4,'2018-03-31 14:42:14','2018-04-07 14:42:23','2018-04-06 14:42:32',NULL,'selesai'),
(20,1,6,'2018-04-03 14:42:54','2018-04-10 14:43:22','2018-04-09 14:43:31',NULL,'selesai'),
(21,1,9,'2018-04-09 14:46:22','2018-04-16 14:46:30','2018-04-15 14:46:44',NULL,'selesai'),
(22,1,1,'2018-04-16 14:47:03','2018-04-23 14:47:18','2018-04-22 14:47:25',NULL,'selesai'),
(23,2,1,'2018-04-24 14:47:43','2018-05-01 14:47:52','2018-04-30 14:48:00',NULL,'selesai'),
(24,8,2,'2018-05-02 14:48:46','2018-05-09 14:48:53','2018-05-08 14:49:00',NULL,'selesai'),
(25,6,4,'2018-05-08 14:50:16','2018-05-15 14:50:24','2018-05-14 14:50:32',NULL,'selesai'),
(26,6,5,'2018-05-14 14:50:47','2018-05-21 14:50:57','2018-05-20 14:51:09',NULL,'selesai'),
(27,6,7,'2018-05-20 14:51:25','2018-05-27 14:51:33','2018-05-26 14:51:46',NULL,'selesai'),
(28,2,8,'2018-05-26 14:52:09','2018-06-02 14:52:18','2018-06-01 14:52:26',NULL,'selesai'),
(30,2,9,'2018-06-03 14:52:55','2018-06-10 14:53:06','2018-06-09 14:53:12',NULL,'selesai'),
(31,3,5,'2018-06-09 14:54:31','2018-06-16 14:54:46','2018-06-15 14:54:53',NULL,'selesai'),
(32,3,2,'2018-06-15 15:08:04','2018-06-22 15:08:12','2018-06-21 15:08:21',NULL,'selesai'),
(33,4,8,'2018-06-21 15:08:42','2018-06-28 15:08:57','2018-06-27 15:09:05',NULL,'selesai'),
(34,4,2,'2018-07-01 15:09:26','2018-07-08 15:09:34','2018-07-07 15:10:06',NULL,'selesai'),
(35,7,1,'2018-07-07 15:10:25','2018-07-14 15:10:32','2018-07-13 15:10:38',NULL,'selesai'),
(36,7,3,'2018-07-13 15:10:55','2018-07-20 15:11:02','2018-07-19 15:11:08',NULL,'selesai'),
(37,2,9,'2018-07-21 15:11:28','2018-07-28 15:11:35','2018-07-27 15:11:41',NULL,'selesai'),
(38,2,8,'2018-07-28 15:12:09','2018-08-04 15:12:17','2018-08-03 15:12:29',NULL,'selesai'),
(39,3,7,'2018-08-05 15:12:52','2018-08-12 15:13:06','2018-08-11 15:13:31',NULL,'selesai'),
(40,1,7,'2018-08-11 15:14:04','2018-08-18 15:14:10','2018-08-17 15:14:19',NULL,'selesai'),
(41,2,5,'2018-08-17 15:14:35','2018-08-24 15:14:42','2018-08-23 15:14:47',NULL,'selesai'),
(42,2,6,'2018-08-23 15:15:10','2018-08-30 15:15:16','2018-08-29 15:15:26',NULL,'selesai'),
(43,3,4,'2018-08-29 15:15:43','2018-09-05 15:15:49','2018-09-04 15:15:56',NULL,'selesai'),
(44,3,5,'2018-09-04 15:16:20','2018-09-11 15:16:26','2018-09-10 15:16:32',NULL,'selesai'),
(45,6,1,'2018-09-12 15:16:51','2018-09-19 15:17:00','2018-09-18 15:17:05',NULL,'selesai'),
(46,2,2,'2018-09-18 15:17:36','2018-09-25 15:17:44','2018-09-24 15:17:57',NULL,'selesai'),
(47,2,4,'2018-09-24 15:18:13','2018-10-01 15:18:22','2018-09-30 15:18:29',NULL,'selesai'),
(48,2,5,'2018-10-01 15:19:01','2018-10-08 15:19:06','2018-10-07 15:19:10',NULL,'selesai'),
(49,1,5,'2018-10-07 15:19:21','2018-10-14 15:19:31','2018-10-13 15:19:36',NULL,'selesai'),
(50,3,6,'2018-10-13 15:19:49','2018-10-20 15:19:59','2018-10-19 15:20:04',NULL,'selesai'),
(51,1,3,'2018-10-20 15:20:21','2018-10-27 15:20:27','2018-10-26 15:20:32',NULL,'selesai'),
(52,1,2,'2018-10-27 15:20:43','2018-11-03 15:20:49','2018-11-02 15:20:56',NULL,'selesai'),
(53,2,5,'2018-11-03 15:21:14','2018-11-10 15:21:19','2018-11-09 15:21:24',NULL,'selesai'),
(54,2,7,'2018-11-10 15:21:35','2018-11-17 15:21:43','2018-11-16 15:21:47',NULL,'selesai'),
(55,2,3,'2018-11-16 15:21:57','2018-11-23 15:22:07',NULL,NULL,'pinjam'),
(56,4,2,'2018-11-18 15:22:25','2018-11-25 15:22:30',NULL,NULL,'pinjam');

/*Table structure for table `penerbit` */

DROP TABLE IF EXISTS `penerbit`;

CREATE TABLE `penerbit` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_penerbit` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `telepon` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `penerbit` */

insert  into `penerbit`(`id`,`nama_penerbit`,`alamat`,`telepon`) values 
(1,'sentosa jaya','denpasar','083128281812'),
(2,'makmur jaya','denpasar','081282123112'),
(3,'galaxy rasi','singaraja','083128281812'),
(4,'andromeda','jakarta','083128281812'),
(5,'sinar bumi','jakarta','083128281812');

/*Table structure for table `pengarang` */

DROP TABLE IF EXISTS `pengarang`;

CREATE TABLE `pengarang` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_pengarang` varchar(30) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  `telepon` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `pengarang` */

insert  into `pengarang`(`id`,`nama_pengarang`,`jenis_kelamin`,`telepon`) values 
(1,'listya','Perempuan','081726757373'),
(2,'sintya an','Perempuan','081726757373'),
(3,'ganjar p','Laki-Laki','081726757373'),
(4,'rikentucky','Laki-Laki','081726757373'),
(5,'dedy ardana','Laki-Laki','081726757373'),
(6,'gunawan','Laki-Laki','081726757373');

/*Table structure for table `rak` */

DROP TABLE IF EXISTS `rak`;

CREATE TABLE `rak` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `kode_rak` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `rak` */

insert  into `rak`(`id`,`kode_rak`) values 
(1,'101'),
(2,'102'),
(3,'201'),
(4,'202'),
(5,'203'),
(6,'301'),
(7,'302');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
