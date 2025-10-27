Create DataBase coursemanagement
create Table course{
    idc int(4) constraint pk_id primary key;
    nomc varchar(15) Not Null ;


};
Create Table eleve{
    idc int(4);
    ide int(4);
    Primary key(idc,ide)
    npe varchar(15) Check('A'<=npe<='Z')
    foreign key idc References course(idc);

}