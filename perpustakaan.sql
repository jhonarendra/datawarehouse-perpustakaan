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
  `id_detail_buku` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_pengarang` (`id_pengarang`),
  KEY `id_penerbit` (`id_penerbit`),
  CONSTRAINT `buku_ibfk_1` FOREIGN KEY (`id_pengarang`) REFERENCES `pengarang` (`id`),
  CONSTRAINT `buku_ibfk_2` FOREIGN KEY (`id_penerbit`) REFERENCES `penerbit` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `buku` */

insert  into `buku`(`id`,`nama_buku`,`sinopsis`,`id_pengarang`,`id_penerbit`,`id_detail_buku`) values 
(1,'java for dummies',NULL,1,1,120),
(2,'android for dummies',NULL,1,1,56),
(3,'tutorial laravel',NULL,1,1,106),
(4,'android exper',NULL,1,1,23),
(5,'create design for web',NULL,2,1,56),
(6,'optimize your SEO',NULL,2,1,56),
(7,'design web',NULL,2,1,56),
(8,'android beginner',NULL,3,2,26),
(9,'android beginner part 2',NULL,3,2,36),
(10,'exper on java part 3',NULL,3,2,56),
(11,'simple biology',NULL,4,3,100),
(12,'natural language processing',NULL,4,3,100),
(13,'information retrieval',NULL,5,4,56),
(14,'mixed reality',NULL,6,5,200);

/*Table structure for table `detail_buku` */

DROP TABLE IF EXISTS `detail_buku`;

CREATE TABLE `detail_buku` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `id_buku` int(10) DEFAULT NULL,
  `kode_barcode` varchar(30) DEFAULT NULL,
  `id_rak` int(10) DEFAULT NULL,
  `jumlah` int(3) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_buku` (`id_buku`),
  KEY `id_rak` (`id_rak`),
  CONSTRAINT `detail_buku_ibfk_1` FOREIGN KEY (`id_buku`) REFERENCES `buku` (`id`),
  CONSTRAINT `detail_buku_ibfk_2` FOREIGN KEY (`id_rak`) REFERENCES `rak` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `detail_buku` */

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
  `id_buku` int(10) DEFAULT NULL,
  `jumlah` int(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_peminjaman` (`id_peminjaman`),
  KEY `id_buku` (`id_buku`),
  CONSTRAINT `detail_peminjaman_ibfk_1` FOREIGN KEY (`id_peminjaman`) REFERENCES `peminjaman` (`id`),
  CONSTRAINT `detail_peminjaman_ibfk_2` FOREIGN KEY (`id_buku`) REFERENCES `buku` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `detail_peminjaman` */

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `peminjaman` */

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `rak` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
