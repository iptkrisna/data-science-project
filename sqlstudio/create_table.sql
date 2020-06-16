create database if not exists bts;
use bts;

drop table if exists covid_ihsg;

create table covid_ihsg (
  TANGGAL date,
  KEY varchar(21),
  JUMLAH_ITEM int,
  JUMLAH_MENINGGAL int,
  JUMLAH_SEMBUH int,
  JUMLAH_POSITIF int,
  JUMLAH_DIRAWAT int,
  JUMLAH_POSITIF_KUM int,
  JUMLAH_SEMBUH_KUM int,
  JUMLAH_MENINGGAL_KUM int,
  JUMLAH_DIRAWAT_KUM int,
  TICKER varchar(21),
  NAME varchar(51),
  OPEN float,
  HIGH float,
  LOW float,
  CLOSE float,
  VOLUME int,
  INDEX (TANGGAL), INDEX (KEY)
);
