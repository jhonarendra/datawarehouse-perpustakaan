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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_buku` */

/*Table structure for table `dim_member` */

DROP TABLE IF EXISTS `dim_member`;

CREATE TABLE `dim_member` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `nama_member` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `dim_member` */

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fact_peminjaman_bulan` */

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
