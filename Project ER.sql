use MiniProject;

drop table Items;
drop table Manufacture;
drop table Inventory;
drop table Customer;
drop table Orders;
drop table Cart;
drop table Bill;

create table Items(
I_ID numeric(4) Primary Key  Not Null,
Name varchar(25),
Type varchar(25),
Price numeric(8,2));


create table Manufacture(
M_ID numeric(5) Primary key Not Null,
I_ID numeric(4), foreign key (I_ID) references Items(I_ID),
M_Price numeric(6,2),
Factory varchar(25),
Address varchar(30));


create table Inventory(
I_ID numeric(4),
M_ID numeric(5),
Quantity int,
foreign key (I_ID) references Items(I_ID) on delete cascade,
foreign key (M_ID) references Manufacture(M_ID) on delete cascade);


create table Customers(
C_ID numeric(3) primary key,
C_Name varchar(30),
C_Phone numeric(10),
C_Address varchar(35));


create table Orders(
O_ID varchar(4) Primary key,
C_ID numeric(3), foreign key (C_ID) references Customers(C_ID));


create table Cart(
Order_No varchar(4), foreign key (Order_No) references Orders(O_ID),
I_ID numeric(4), foreign key (I_ID) references Items(I_ID),
Quantity int,
Item_Price int);


create table Bill(
B_ID varchar(4) primary key,
C_ID numeric(3),  foreign key (C_ID) references Customers(C_ID),
Total_Price int,
Order_Date date);


insert into Items values (1111,"Water","Beverages",10);
insert into Items values (1112,"Soft Drink","Beverages",20);
insert into Items values (1113,"Coffee","Beverages",25);
insert into Items values (2221,"Chips","Snacks",10);
insert into Items values (2222,"Chocolate","Snacks",200);
insert into Items values (2223,"Biscuits","Snacks",60);
insert into Items values (3331,"Pen","Stationary",10);
insert into Items values (3332,"Notebook","Stationary",80);
insert into Items values (3333,"Papers","Stationary",45);
insert into Items values (4441,"Soap","Bathroom",65);
insert into Items values (4442,"Shampoo","Bathroom",175);
insert into Items values (5551,"Batteries","Others",120);
insert into Items values (6661,"Hand Bags","Fashion",2750);
insert into Items values (6662,"Tshirt","Fashion",3950);




insert into Manufacture values (10111,1111,3,"CocoCola","Mumbai");
insert into Manufacture values (10112,1112,12,"CocoCola","Mumbai");
insert into Manufacture values (10113,1113,20,"StarBucks","Bangalore");
insert into Manufacture values (20221,2221,6,"Lays","Pune");
insert into Manufacture values (20222,2222,150,"DairyMilk","Bangalore");
insert into Manufacture values (20223,2223,30,"DairyMilk","Bangalore");
insert into Manufacture values (30331,3331,4,"Classmate","Ahmedabad");
insert into Manufacture values (30332,3332,50,"CLassmate","Ahmedabad");
insert into Manufacture values (30333,3333,20,"Classmate","Ahmedabad");
insert into Manufacture values (40441,4441,45,"SunSilk","Delhi");
insert into Manufacture values (40442,4442,120,"SunSilk","Delhi");
insert into Manufacture values (50551,5551,100,"Duracell","Delhi");
insert into Manufacture values (60661,6661,750,"Louis Vuitton","Bangalore");
insert into Manufacture values (60662,6662,1450,"Calvin Klein","Mumbai");



insert into inventory values (1111,10111,250);
insert into inventory values (1112,10112,180);
insert into inventory values (1113,10113,105);
insert into inventory values (2221,20221,250);
insert into inventory values (2222,20222,120);
insert into inventory values (2223,20223,145);
insert into inventory values (3331,30331,300);
insert into inventory values (3332,30332,200);
insert into inventory values (3333,30333,350);
insert into inventory values (4441,40441,160);
insert into inventory values (4442,40442,150);
insert into inventory values (5551,50551,250);
insert into inventory values (6661,60661,105);
insert into inventory values (6662,60662,105);

insert into Customers values (001,"Arya",9513304051,"Bangalore");
insert into Customers values (002,"Aniket",8839368419,"Bhopal");
insert into Customers values (003,"Kaven",9033303071,"Ahmedabad");
insert into Customers values (004,"Sotbik",6969420694,"Pune");

insert into Orders values ('OR01',001);
insert into Orders values ('OR02',002);
insert into Orders values ('OR03',003);
insert into Orders values ('OR04',004);










