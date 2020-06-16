create database if not exists bts;
use bts;

drop table if exists covid_ihsg;

create table covid_ihsg (
  TANGGAL date,
  KEY varchar(21),
  JUMLAH_ITEM integer,
  JUMLAH_MENINGGAL integer,
  JUMLAH_SEMBUH integer,
  JUMLAH_POSITIF integer,
  JUMLAH_DIRAWAT integer,
  JUMLAH_POSITIF_KUM integer,
  JUMLAH_SEMBUH_KUM integer,
  JUMLAH_MENINGGAL_KUM integer,
  JUMLAH_DIRAWAT_KUM integer,
  TICKER varchar(21),
  NAME varchar(51),
  OPEN float,
  HIGH float,
  LOW float,
  CLOSE float,
  VOLUME integer,
  INDEX (TANGGAL), INDEX (KEY)
);
