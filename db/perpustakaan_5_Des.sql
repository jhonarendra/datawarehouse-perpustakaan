/*
SQLyog Ultimate v12.4.3 (64 bit)
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

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
(14,'mixed reality',NULL,6,5),
(15,'1001 cara menjadi kaya',NULL,1,1),
(16,'1001 cara mengatasi error',NULL,1,2);

/*Table structure for table `cb_perpustakaan` */

DROP TABLE IF EXISTS `cb_perpustakaan`;

CREATE TABLE `cb_perpustakaan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_perpustakaan` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `cb_perpustakaan` */

insert  into `cb_perpustakaan`(`id`,`nama_perpustakaan`,`alamat`) values 
(1,'perpustakaan bersama',NULL),
(2,'perpustakaan fakultas',NULL),
(3,'perpustakaan terbuka',NULL),
(4,'perpustakaan jurusan',NULL);

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
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;

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
(51,26,19),
(52,57,1);

/*Table structure for table `member` */

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_member` varchar(30) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `telepon` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

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
(9,'anunya','Perempuan','singaraja','082616152628'),
(10,'bagus','Laki-Laki','badung','087682129000'),
(11,'agung','Laki-Laki','agung','082919219298'),
(12,'bagas','Laki-Laki','badung','092019021993'),
(13,'anjeng','Perempuan','badung','019209010200'),
(14,'angung','Perempuan','badung','019209092010'),
(15,'elo','Laki-Laki','gianyar','098291281291'),
(16,'sebastian','Laki-Laki','badung','029102901920'),
(17,'cok','Laki-Laki','badung','092092019202'),
(18,'agung','Laki-Laki','badung','019292010292'),
(19,'wahyudi','Laki-Laki','badung','087217828122');

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
  `id_perpustakaan` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_pegawai` (`id_pegawai`),
  KEY `id_member` (`id_member`),
  KEY `id_perpustakaan` (`id_perpustakaan`),
  CONSTRAINT `peminjaman_ibfk_1` FOREIGN KEY (`id_pegawai`) REFERENCES `pegawai` (`id`),
  CONSTRAINT `peminjaman_ibfk_2` FOREIGN KEY (`id_member`) REFERENCES `member` (`id`),
  CONSTRAINT `peminjaman_ibfk_3` FOREIGN KEY (`id_perpustakaan`) REFERENCES `cb_perpustakaan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;

/*Data for the table `peminjaman` */

insert  into `peminjaman`(`id`,`id_pegawai`,`id_member`,`tgl_pinjam`,`tgl_harus_kembali`,`tgl_kembali`,`denda`,`status`,`id_perpustakaan`) values 
(1,1,1,'2018-11-17 21:43:34','2018-11-24 21:43:37',NULL,NULL,'pinjam',1),
(2,1,2,'2018-01-01 14:20:39','2018-01-08 14:20:55','2018-01-07 14:25:56',NULL,'selesai',2),
(3,1,3,'2018-01-02 14:21:25','2018-01-09 14:21:37','2018-01-08 14:26:16',NULL,'selesai',3),
(4,2,4,'2018-01-03 14:24:50','2018-01-10 14:25:00','2018-01-09 14:26:29',NULL,'selesai',1),
(5,2,5,'2018-01-04 14:26:47','2018-01-11 14:27:16','2018-01-10 14:27:35',NULL,'selesai',2),
(6,2,6,'2018-01-05 14:28:03','2018-01-12 14:28:15','2018-01-11 14:29:08',NULL,'selesai',3),
(7,3,7,'2018-01-06 14:29:29','2018-01-13 14:29:39','2018-01-12 14:29:50',NULL,'selesai',1),
(8,2,8,'2018-01-07 14:30:12','2018-01-14 14:30:21','2018-01-13 14:30:37',NULL,'selesai',2),
(9,3,9,'2018-01-08 14:30:59','2018-01-15 14:31:07','2018-01-14 14:31:18',NULL,'selesai',3),
(10,4,1,'2018-02-01 14:35:22','2018-02-08 14:35:30','2018-02-07 14:35:38',NULL,'selesai',1),
(11,4,3,'2018-02-05 14:35:59','2018-02-12 14:36:10','2018-02-11 14:36:19',NULL,'selesai',1),
(12,4,5,'2018-02-13 14:36:42','2018-02-20 14:36:53','2018-02-19 14:37:01',NULL,'selesai',1),
(13,4,1,'2018-02-10 14:37:45','2018-02-17 14:37:57','2018-02-16 14:38:06',NULL,'selesai',2),
(14,4,1,'2018-02-19 14:38:31','2018-02-26 14:38:46','2018-02-25 14:38:56',NULL,'selesai',2),
(15,5,2,'2018-03-05 14:39:16','2018-03-12 14:39:26','2018-03-11 14:39:35',NULL,'selesai',2),
(16,5,4,'2018-03-07 14:40:11','2018-03-14 14:40:24','2018-03-13 14:40:32',NULL,'selesai',3),
(17,5,9,'2018-03-15 14:40:50','2018-03-22 14:40:58','2018-03-21 14:41:08',NULL,'selesai',3),
(18,5,4,'2018-03-22 14:41:26','2018-03-29 14:41:36','2018-03-28 14:41:46',NULL,'selesai',3),
(19,1,4,'2018-03-31 14:42:14','2018-04-07 14:42:23','2018-04-06 14:42:32',NULL,'selesai',3),
(20,1,6,'2018-04-03 14:42:54','2018-04-10 14:43:22','2018-04-09 14:43:31',NULL,'selesai',2),
(21,1,9,'2018-04-09 14:46:22','2018-04-16 14:46:30','2018-04-15 14:46:44',NULL,'selesai',1),
(22,1,1,'2018-04-16 14:47:03','2018-04-23 14:47:18','2018-04-22 14:47:25',NULL,'selesai',3),
(23,2,1,'2018-04-24 14:47:43','2018-05-01 14:47:52','2018-04-30 14:48:00',NULL,'selesai',2),
(24,8,2,'2018-05-02 14:48:46','2018-05-09 14:48:53','2018-05-08 14:49:00',NULL,'selesai',1),
(25,6,4,'2018-05-08 14:50:16','2018-05-15 14:50:24','2018-05-14 14:50:32',NULL,'selesai',3),
(26,6,5,'2018-05-14 14:50:47','2018-05-21 14:50:57','2018-05-20 14:51:09',NULL,'selesai',2),
(57,1,1,'2018-11-29 17:20:34','2018-11-29 17:20:36','2018-11-29 17:20:38',NULL,'selesai',1);

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
