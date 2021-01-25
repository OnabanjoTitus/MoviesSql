create database movie_database;
show databases;
use movie_database;
create table actor(
act_id integer not null primary key auto_increment,
act_fname char(20),
act_lname char(20),
act_gender char(1)
);
create table director(
dir_id integer not null primary key auto_increment,
dir_fname char(20),
dir_lname char(20)
);
create table movie(
mov_id integer not null primary key auto_increment,
mov_title char(50),
mov_year integer,
mov_time integer,
mov_lang char(50),
mov_dt_rel date,
mov_rel_country char(5)
);
create table reviewer(
rev_id integer not null primary key auto_increment,
rev_name char(30)
);
create table genres(
gen_id integer not null primary key auto_increment,
gen_title char(20)
);
create table movie_direction(
dir_id integer,
mov_id integer,
foreign key(dir_id) references director(dir_id),
foreign key(mov_id) references movie(mov_id)
);
 create table movie_cast(
 act_id integer,
 mov_id integer,
 role char(30),
 foreign key(act_id) 
 	references actor(act_id),
 foreign key(mov_id) 
 	references director(dir_id)
 );
create table movie_genres(
mov_id integer,
gen_id integer,
foreign key(mov_id) references movie(mov_id),
foreign key(gen_id) references genres(gen_id)
);
create table rating(
mov_id integer,
rev_id integer,
rev_stars integer,
num_o_ratings integer,
foreign key(mov_id) references movie(mov_id),
foreign key(rev_id) references reviewer(rev_id)
);