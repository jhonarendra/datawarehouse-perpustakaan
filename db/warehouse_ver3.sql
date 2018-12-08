/*
SQLyog Ultimate v12.5.0 (64 bit)
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

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
(16,'1001 cara mengatasi error','listya','makmur jaya'),
(17,'PyQt6','ganjar p','sentosa jaya'),
(19,'Python Expert','dedy ardana','makmur jaya'),
(20,'1010','listya','sentosa jaya');

/*Table structure for table `dim_member` */

DROP TABLE IF EXISTS `dim_member`;

CREATE TABLE `dim_member` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_member` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

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
(19,'wahyudi','badung','Laki-Laki'),
(20,'perdana','gianyar','Laki-Laki');

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
(4,'perpustakaan jurusan','None'),
(5,'perpustakaan keliling','None');

/*Table structure for table `fact_peminjaman_bulan` */

DROP TABLE IF EXISTS `fact_peminjaman_bulan`;

CREATE TABLE `fact_peminjaman_bulan` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_dimBuku` int(10) DEFAULT NULL,
  `id_dimMember` int(10) DEFAULT NULL,
  `id_dimPerpustakaan` int(10) DEFAULT NULL,
  `tahun` varchar(4) DEFAULT NULL,
  `bulan` varchar(10) DEFAULT NULL,
  `tanggal` varchar(3) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_dimBuku` (`id_dimBuku`),
  KEY `id_dimMember` (`id_dimMember`),
  KEY `id_dimPerpustakaan` (`id_dimPerpustakaan`),
  CONSTRAINT `fact_peminjaman_bulan_ibfk_1` FOREIGN KEY (`id_dimBuku`) REFERENCES `dim_buku` (`id`),
  CONSTRAINT `fact_peminjaman_bulan_ibfk_2` FOREIGN KEY (`id_dimMember`) REFERENCES `dim_member` (`id`),
  CONSTRAINT `fact_peminjaman_bulan_ibfk_3` FOREIGN KEY (`id_dimPerpustakaan`) REFERENCES `dim_perpustakaan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

/*Data for the table `fact_peminjaman_bulan` */

insert  into `fact_peminjaman_bulan`(`id`,`id_dimBuku`,`id_dimMember`,`id_dimPerpustakaan`,`tahun`,`bulan`,`tanggal`,`jumlah`) values 
(1,2,4,1,'2018','January','3',1),
(2,1,2,2,'2018','January','1',2),
(3,2,7,1,'2018','January','6',1),
(4,4,5,2,'2018','January','5',1),
(5,1,8,2,'2018','January','7',1),
(6,2,3,3,'2018','January','2',1),
(7,3,4,1,'2018','January','3',1),
(8,3,5,2,'2018','January','4',2),
(9,3,5,2,'2018','January','5',2),
(10,1,3,3,'2018','January','2',1),
(11,1,9,3,'2018','January','8',1),
(12,1,3,1,'2018','February','5',1),
(13,3,5,1,'2018','February','13',1),
(14,3,1,2,'2018','February','19',1),
(15,2,1,1,'2018','February','1',1),
(16,2,3,1,'2018','February','5',1),
(17,1,1,2,'2018','February','10',1),
(18,1,4,3,'2018','March','22',2),
(19,3,4,3,'2018','March','31',2),
(20,1,4,3,'2018','March','7',1),
(21,4,2,2,'2018','March','5',1),
(22,9,4,3,'2018','March','22',1),
(23,2,4,3,'2018','March','22',1),
(24,5,2,2,'2018','March','5',1),
(25,3,9,3,'2018','March','15',1),
(26,1,6,2,'2018','April','3',3),
(27,5,1,2,'2018','April','24',1),
(28,3,9,1,'2018','April','9',1),
(29,4,1,2,'2018','April','24',1),
(30,1,1,3,'2018','April','16',2),
(31,1,9,1,'2018','April','9',2),
(32,3,2,1,'2018','May','2',1),
(33,6,5,2,'2018','May','14',1),
(34,3,4,3,'2018','May','8',2),
(35,3,5,2,'2018','May','14',1),
(36,1,4,3,'2018','May','8',1),
(37,1,1,1,'2018','November','17',1),
(38,2,1,1,'2018','November','17',1),
(39,1,1,1,'2018','November','29',1);

/*Table structure for table `fact_peminjaman_tahun` */

DROP TABLE IF EXISTS `fact_peminjaman_tahun`;

CREATE TABLE `fact_peminjaman_tahun` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `id_dimBuku` int(5) DEFAULT NULL,
  `id_dimMember` int(5) DEFAULT NULL,
  `id_dimPerpustakaan` int(5) DEFAULT NULL,
  `bulan` varchar(30) DEFAULT NULL,
  `tahun` varchar(30) DEFAULT NULL,
  `jumlah` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_DimBuku` (`id_dimBuku`),
  KEY `id_DimMember` (`id_dimMember`),
  KEY `id_DimPerpustakaan` (`id_dimPerpustakaan`),
  CONSTRAINT `fact_peminjaman_tahun_ibfk_1` FOREIGN KEY (`id_DimBuku`) REFERENCES `dim_buku` (`id`),
  CONSTRAINT `fact_peminjaman_tahun_ibfk_2` FOREIGN KEY (`id_DimMember`) REFERENCES `dim_member` (`id`),
  CONSTRAINT `fact_peminjaman_tahun_ibfk_3` FOREIGN KEY (`id_DimPerpustakaan`) REFERENCES `dim_perpustakaan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

/*Data for the table `fact_peminjaman_tahun` */

insert  into `fact_peminjaman_tahun`(`id`,`id_dimBuku`,`id_dimMember`,`id_dimPerpustakaan`,`bulan`,`tahun`,`jumlah`) values 
(1,3,4,1,'January','2018',1),
(2,2,3,3,'January','2018',1),
(3,3,5,2,'January','2018',4),
(4,1,8,2,'January','2018',1),
(5,2,4,1,'January','2018',1),
(6,2,7,1,'January','2018',1),
(7,1,3,3,'January','2018',1),
(8,1,9,3,'January','2018',1),
(9,1,2,2,'January','2018',2),
(10,4,5,2,'January','2018',1),
(11,1,1,2,'February','2018',1),
(12,2,1,1,'February','2018',1),
(13,2,3,1,'February','2018',1),
(14,3,1,2,'February','2018',1),
(15,1,3,1,'February','2018',1),
(16,3,5,1,'February','2018',1),
(17,5,2,2,'March','2018',1),
(18,1,4,3,'March','2018',3),
(19,9,4,3,'March','2018',1),
(20,3,4,3,'March','2018',2),
(21,4,2,2,'March','2018',1),
(22,3,9,3,'March','2018',1),
(23,2,4,3,'March','2018',1),
(24,1,1,3,'April','2018',2),
(25,1,6,2,'April','2018',3),
(26,5,1,2,'April','2018',1),
(27,1,9,1,'April','2018',2),
(28,4,1,2,'April','2018',1),
(29,3,9,1,'April','2018',1),
(30,1,4,3,'May','2018',1),
(31,6,5,2,'May','2018',1),
(32,3,2,1,'May','2018',1),
(33,3,4,3,'May','2018',2),
(34,3,5,2,'May','2018',1),
(35,2,1,1,'November','2018',1),
(36,1,1,1,'November','2018',2);

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `history_etl` */

insert  into `history_etl`(`id`,`id_tabel`,`start_row`,`end_row`,`status`,`tgl_proses`) values 
(1,5,1,20,'sukses','2018-12-07 15:20:34'),
(2,1,1,20,'sukses','2018-12-07 15:20:34'),
(3,2,1,5,'sukses','2018-12-07 15:20:34'),
(4,7,1,57,'sukses','2018-12-07 15:20:34');

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
