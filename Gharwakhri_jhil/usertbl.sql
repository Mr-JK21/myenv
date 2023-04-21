create table usertbl(
    id int(11) primary key auto_increment,
    usernm varchar(21) not null,
    passwd varchar(31) not null,
    role varchar(6) not null,
    email varchar(31) not null,
    phone varchar(10) not null,
    city varchar(31) not null,
    favque varchar(41) not null,
    status varchar(21) not null

);