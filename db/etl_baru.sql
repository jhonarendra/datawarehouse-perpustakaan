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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

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
(14,'mixed reality','gunawan','sinar bumi'),
(15,'1001 cara menjadi kaya','listya','sentosa jaya'),
(16,'1001 cara mengatasi error','listya','makmur jaya');

/*Table structure for table `dim_member` */

DROP TABLE IF EXISTS `dim_member`;

CREATE TABLE `dim_member` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_member` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

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
(9,'anunya','singaraja','Perempuan'),
(10,'bagus','badung','Laki-Laki'),
(11,'agung','agung','Laki-Laki'),
(12,'bagas','badung','Laki-Laki'),
(13,'anjeng','badung','Perempuan'),
(14,'angung','badung','Perempuan'),
(15,'elo','gianyar','Laki-Laki'),
(16,'sebastian','badung','Laki-Laki'),
(17,'cok','badung','Laki-Laki'),
(18,'agung','badung','Laki-Laki'),
(19,'wahyudi','badung','Laki-Laki');

/*Table structure for table `dim_perpustakaan` */

DROP TABLE IF EXISTS `dim_perpustakaan`;

CREATE TABLE `dim_perpustakaan` (
  `id` int(5) NOT NULL,
  `nama_perpustakaan` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_perpustakaan` */

insert  into `dim_perpustakaan`(`id`,`nama_perpustakaan`,`alamat`) values 
(1,'perpustakaan bersama','None'),
(2,'perpustakaan fakultas','None'),
(3,'perpustakaan terbuka','None'),
(4,'perpustakaan jurusan','None');

/*Table structure for table `fact_peminjaman_bulan` */

DROP TABLE IF EXISTS `fact_peminjaman_bulan`;

CREATE TABLE `fact_peminjaman_bulan` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_dimBuku` int(10) DEFAULT NULL,
  `id_dimMember` int(10) DEFAULT NULL,
  `id_dimPerpustakaan` int(10) DEFAULT NULL,
  `tahun` varchar(4) DEFAULT NULL,
  `bulan` varchar(10) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_dimBuku` (`id_dimBuku`),
  KEY `id_dimMember` (`id_dimMember`),
  KEY `id_dimPerpustakaan` (`id_dimPerpustakaan`),
  CONSTRAINT `fact_peminjaman_bulan_ibfk_1` FOREIGN KEY (`id_dimBuku`) REFERENCES `dim_buku` (`id`),
  CONSTRAINT `fact_peminjaman_bulan_ibfk_2` FOREIGN KEY (`id_dimMember`) REFERENCES `dim_member` (`id`),
  CONSTRAINT `fact_peminjaman_bulan_ibfk_3` FOREIGN KEY (`id_dimPerpustakaan`) REFERENCES `dim_perpustakaan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=latin1;

/*Data for the table `fact_peminjaman_bulan` */

insert  into `fact_peminjaman_bulan`(`id`,`id_dimBuku`,`id_dimMember`,`id_dimPerpustakaan`,`tahun`,`bulan`,`jumlah`) values 
(113,1,8,2,'2018','January',1),
(114,1,2,2,'2018','January',2),
(115,2,7,1,'2018','January',1),
(116,2,4,1,'2018','January',1),
(117,1,6,3,'2018','January',1),
(118,2,3,3,'2018','January',1),
(119,3,5,2,'2018','January',2),
(120,3,4,1,'2018','January',1),
(121,1,9,3,'2018','January',1),
(122,4,6,3,'2018','January',2),
(123,1,3,3,'2018','January',1),
(124,3,1,2,'2018','February',1),
(125,3,5,1,'2018','February',1),
(126,1,3,1,'2018','February',1),
(127,1,1,2,'2018','February',1),
(128,2,3,1,'2018','February',1),
(129,2,1,1,'2018','February',1),
(130,4,2,2,'2018','March',1),
(131,3,4,3,'2018','March',2),
(132,9,4,3,'2018','March',1),
(133,1,4,3,'2018','March',3),
(134,5,2,2,'2018','March',1),
(135,2,4,3,'2018','March',1),
(136,3,9,3,'2018','March',1),
(137,4,1,2,'2018','April',1),
(138,3,9,1,'2018','April',1),
(139,5,1,2,'2018','April',1),
(140,1,6,2,'2018','April',3),
(141,1,9,1,'2018','April',2),
(142,1,1,3,'2018','April',2),
(143,3,4,3,'2018','May',2),
(144,6,5,2,'2018','May',1),
(145,3,2,1,'2018','May',1),
(146,1,4,3,'2018','May',1),
(147,3,5,2,'2018','May',1),
(148,1,1,1,'2018','November',2),
(149,2,1,1,'2018','November',1);

/*Table structure for table `fact_peminjaman_tahun` */

DROP TABLE IF EXISTS `fact_peminjaman_tahun`;

CREATE TABLE `fact_peminjaman_tahun` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_dimBuku` int(10) DEFAULT NULL,
  `id_dimMember` int(10) DEFAULT NULL,
  `id_dimPerpustakaan` int(10) DEFAULT NULL,
  `tahun` varchar(4) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_dimBuku` (`id_dimBuku`),
  KEY `id_dimMember` (`id_dimMember`),
  KEY `id_dimPerpustakaan` (`id_dimPerpustakaan`),
  CONSTRAINT `fact_peminjaman_tahun_ibfk_1` FOREIGN KEY (`id_dimBuku`) REFERENCES `dim_buku` (`id`),
  CONSTRAINT `fact_peminjaman_tahun_ibfk_2` FOREIGN KEY (`id_dimMember`) REFERENCES `dim_member` (`id`),
  CONSTRAINT `fact_peminjaman_tahun_ibfk_3` FOREIGN KEY (`id_dimPerpustakaan`) REFERENCES `dim_perpustakaan` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fact_peminjaman_tahun` */

/*Table structure for table `history_etl` */

DROP TABLE IF EXISTS `history_etl`;

CREATE TABLE `history_etl` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_tabel` int(10) DEFAULT NULL,
  `start_row` int(10) DEFAULT NULL,
  `end_row` int(10) DEFAULT NULL,
  `status` enum('sukses','gagal') DEFAULT NULL,
  `tgl_proses` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_tabel` (`id_tabel`),
  CONSTRAINT `history_etl_ibfk_1` FOREIGN KEY (`id_tabel`) REFERENCES `tb_tabel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

/*Data for the table `history_etl` */

insert  into `history_etl`(`id`,`id_tabel`,`start_row`,`end_row`,`status`,`tgl_proses`) values 
(22,5,1,16,'sukses','2018-11-30 13:07:00'),
(24,2,1,4,'sukses','2018-11-30 13:07:00'),
(26,1,1,16,'sukses','2018-11-30 13:13:37'),
(27,7,1,57,'sukses','2018-11-30 13:24:27'),
(28,5,17,18,'sukses','2018-11-30 14:02:16'),
(29,5,19,19,'sukses','2018-12-03 10:39:04');

/*Table structure for table `tb_tabel` */

DROP TABLE IF EXISTS `tb_tabel`;

CREATE TABLE `tb_tabel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_tabel` varchar(20) DEFAULT NULL,
  `keterangan` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `tb_tabel` */

insert  into `tb_tabel`(`id`,`nama_tabel`,`keterangan`) values 
(1,'buku',NULL),
(2,'cb_perpustakaan',NULL),
(3,'detail_buku',NULL),
(4,'detail_peminjaman',NULL),
(5,'member',NULL),
(6,'pegawai',NULL),
(7,'peminjaman',NULL),
(8,'penerbit',NULL),
(9,'pengarang',NULL),
(10,'rak',NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
