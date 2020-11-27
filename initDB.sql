use coffeeexpress


create table coffeeConsumers(
    -> id int NOT NULL auto_increment,
    -> firstname varchar(100),
    -> lastname varchar(100),
    -> postcode int,
    -> PRIMARY KEY (id)
    -> );