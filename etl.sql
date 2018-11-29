/*
SQLyog Ultimate v12.4.3 (64 bit)
MySQL - 10.1.35-MariaDB : Database - warehouse
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`warehouse` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `warehouse`;

/*Table structure for table `dim_buku` */

DROP TABLE IF EXISTS `dim_buku`;

CREATE TABLE `dim_buku` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_buku` varchar(30) DEFAULT NULL,
  `nama_pengarang` varchar(30) DEFAULT NULL,
  `nama_penerbit` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `dim_buku` */

insert  into `dim_buku`(`id`,`nama_buku`,`nama_pengarang`,`nama_penerbit`) values 
(1,'java for dummies','listya','sentosa jaya'),
(2,'android for dummies','listya','sentosa jaya'),
(3,'tutorial laravel','listya','sentosa jaya'),
(4,'android exper','listya','sentosa jaya'),
(5,'create design for web','sintya an','sentosa jaya'),
(6,'optimize your SEO','sintya an','sentosa jaya'),
(7,'design web','sintya an','sentosa jaya'),
(8,'android beginner','ganjar p','makmur jaya'),
(9,'android beginner part 2','ganjar p','makmur jaya'),
(10,'exper on java part 3','ganjar p','makmur jaya'),
(11,'simple biology','rikentucky','galaxy rasi'),
(12,'natural language processing','rikentucky','galaxy rasi'),
(13,'information retrieval','dedy ardana','andromeda'),
(14,'mixed reality','gunawan','sinar bumi');

/*Table structure for table `dim_member` */

DROP TABLE IF EXISTS `dim_member`;

CREATE TABLE `dim_member` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_member` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `dim_member` */

insert  into `dim_member`(`id`,`nama_member`,`alamat`,`jenis_kelamin`) values 
(1,'deva','badung','Perempuan'),
(2,'agus','denpasar','Laki-Laki'),
(3,'anang','jakarta','Laki-Laki'),
(4,'budi','jimbaran','Laki-Laki'),
(5,'budiman','klungkung','Laki-Laki'),
(6,'raisa','badung','Perempuan'),
(7,'andini','gianyar','Perempuan'),
(8,'natasya','bangli','Perempuan'),
(9,'anunya','singaraja','Perempuan');

/*Table structure for table `fact_peminjaman_bulan` */

DROP TABLE IF EXISTS `fact_peminjaman_bulan`;

CREATE TABLE `fact_peminjaman_bulan` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_dimBuku` int(10) DEFAULT NULL,
  `id_dimMember` int(10) DEFAULT NULL,
  `tahun` varchar(4) DEFAULT NULL,
  `bulan` varchar(10) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_dimBuku` (`id_dimBuku`),
  KEY `id_dimMember` (`id_dimMember`),
  CONSTRAINT `fact_peminjaman_bulan_ibfk_1` FOREIGN KEY (`id_dimBuku`) REFERENCES `dim_buku` (`id`),
  CONSTRAINT `fact_peminjaman_bulan_ibfk_2` FOREIGN KEY (`id_dimMember`) REFERENCES `dim_member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=latin1;

/*Data for the table `fact_peminjaman_bulan` */

insert  into `fact_peminjaman_bulan`(`id`,`id_dimBuku`,`id_dimMember`,`tahun`,`bulan`,`jumlah`) values 
(112,1,6,'2018','January',1),
(113,2,7,'2018','January',1),
(114,4,6,'2018','January',2),
(115,1,8,'2018','January',1),
(116,3,4,'2018','January',1),
(117,1,2,'2018','January',2),
(118,2,4,'2018','January',1),
(119,2,3,'2018','January',1),
(120,1,3,'2018','January',1),
(121,1,9,'2018','January',1),
(122,3,5,'2018','January',2),
(123,2,1,'2018','February',1),
(124,3,1,'2018','February',1),
(125,1,3,'2018','February',1),
(126,1,1,'2018','February',1),
(127,2,3,'2018','February',1),
(128,3,5,'2018','February',1),
(129,3,4,'2018','March',2),
(130,5,2,'2018','March',1),
(131,4,2,'2018','March',1),
(132,3,9,'2018','March',1),
(133,1,4,'2018','March',3),
(134,9,4,'2018','March',1),
(135,2,4,'2018','March',1),
(136,5,1,'2018','April',1),
(137,4,1,'2018','April',1),
(138,1,1,'2018','April',2),
(139,1,6,'2018','April',3),
(140,1,9,'2018','April',2),
(141,3,9,'2018','April',1),
(142,3,5,'2018','May',1),
(143,3,2,'2018','May',1),
(144,6,5,'2018','May',1),
(145,3,4,'2018','May',2),
(146,1,4,'2018','May',1),
(147,1,1,'2018','November',1),
(148,2,1,'2018','November',1);

/*Table structure for table `fact_peminjaman_tahun` */

DROP TABLE IF EXISTS `fact_peminjaman_tahun`;

CREATE TABLE `fact_peminjaman_tahun` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_dimBuku` int(10) DEFAULT NULL,
  `id_dimMember` int(10) DEFAULT NULL,
  `tahun` varchar(4) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_dimBuku` (`id_dimBuku`),
  KEY `id_dimMember` (`id_dimMember`),
  CONSTRAINT `fact_peminjaman_tahun_ibfk_1` FOREIGN KEY (`id_dimBuku`) REFERENCES `dim_buku` (`id`),
  CONSTRAINT `fact_peminjaman_tahun_ibfk_2` FOREIGN KEY (`id_dimMember`) REFERENCES `dim_member` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fact_peminjaman_tahun` */

/*Table structure for table `history_etl` */

DROP TABLE IF EXISTS `history_etl`;

CREATE TABLE `history_etl` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_fact` int(10) DEFAULT NULL,
  `tanggal_mulai` date DEFAULT NULL,
  `tanggal_akhir` date DEFAULT NULL,
  `jumlah_data` int(11) DEFAULT NULL,
  `keterangan` enum('bulanan','tahunan') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_fact` (`id_fact`),
  CONSTRAINT `history_etl_ibfk_1` FOREIGN KEY (`id_fact`) REFERENCES `fact_peminjaman_bulan` (`id`),
  CONSTRAINT `history_etl_ibfk_2` FOREIGN KEY (`id_fact`) REFERENCES `fact_peminjaman_tahun` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `history_etl` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
