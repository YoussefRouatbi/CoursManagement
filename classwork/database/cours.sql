Create DataBase coursemanagement;
use coursemanagement;

CREATE TABLE course (
    idc INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    subtitle TEXT,
    file_path VARCHAR(255)
);


Create Table users(
    idu int auto_increment primary key,
    email varchar(255) not null,
    username varchar(15) not null,
    user_password varchar(255) not null,
    date_insc date default current_date
);

create table matier(
    idm int auto_increment primary key,
    nameMatier varchar(20) check(nameMatier in ('algo','sti','math','phy','lang','opt'))
);

create table matierCour(
    idm int,
    idc int,
    primary key(idm,idc),
    foreign key (idm) references matier(idm) on delete cascade on update cascade,
    foreign key (idc) references course(idc) on delete cascade on update cascade,
    date_added date default current_date
);