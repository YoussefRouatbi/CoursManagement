Create DataBase coursemanagement;
use coursemanagement;

CREATE TABLE course (
    idc INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    subtitle TEXT,
    file_path VARCHAR(255),
    file_type VARCHAR(20) NOT NULL,
    idm int references matier(idm) on delete cascade on update cascade
);


Create Table users(
    idu int auto_increment primary key,
    username varchar(15) unique not null,
    user_password varchar(255) not null,
    date_insc date default current_date
);

create table matier(
    idm int auto_increment primary key,
    nameMatier varchar(20) check(nameMatier in ('algo','sti','math','phy','lang','opt'))
);
