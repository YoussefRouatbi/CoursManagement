Create DataBase coursemanagement;
use coursemanagement;

create table matier(
    idm int auto_increment primary key,
    nameMatier varchar(20)
);

CREATE TABLE course (
    idc INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    subtitle TEXT,
    file_path VARCHAR(255),
    file_url VARCHAR(255),
    idm int ,
    foreign key (idm) references matier(idm) on delete cascade on update cascade
);


Create Table users(
    idu int auto_increment primary key,
    username varchar(15) unique not null,
    user_password varchar(255) not null,
    typeUser varchar(10) default 'user' CHECK (typeUser IN ('admin', 'user')),
    date_insc datetime default CURRENT_TIMESTAMP
);

