## Data-Representation Project 2020
## Student : Michelle Moran

File index : 

|        FILE NAME        |                                               DESCRIPTION                                                |
|:-----------------------:|:--------------------------------------------------------------------------------------------------------:|
| server.py               | Web server for local host                                                                                |
| CoffeeexpertsDAO.py     | Data Access Object file for interacting with the coffeeconsumers database                                |
| CoffeeExperts Orders.py | Testing database connection                                                                              |
| Index.html              | In staticpages folder - Home page that will facilitate the update/creation/deletion of consumer details  |














<table>
<thead>
<tr>
<th>Action</th>
<th>Method</th>
<th>URL</th>
<th>Sample Params</th> 
<th>Sample Return</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get All</td>
<td>GET</td>
<td>/groceries</td>
<td>none</td>
<td>[{...},{...},{...}]</td>  
</tr>
<tr>
<td>Find by id</td>
<td>GET</td>
<td>/groceries/id</td>
<td>none</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode":"xxx"}]
</td> 
<tr>
<td>Create</td>
<td>POST</td>
<td>/groceries</td>
<td>{"Firstname":"xxx"},{"Lastname":"xxx","Postcode:"xxx"}</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode":"xxx"}]
</td>
</tr>
<tr>
<td>Update</td>
<td>PUT</td>
<td>/groceries/id</td>
<td>{"Postcode:"xxx"}</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode:"xxx"}]
</td>
</tr>
<td>Delete</td>
<td>DELETE</td>
<td>/groceries/id</td>
<td>none</td>
<td>{"done:"true}
</td>
</tr>  
</tbody>
</table>


### MySQL Database : coffeeexpress

Two tables created  :

- coffeeconsumers
- consumerorders

#### MySQL command to create tables :

CREATE TABLE members( id int NOT NULL AUTO_INCREMENT, firstname VARCHAR(100), lastname VARCHAR(100), postcode VARCHAR(100), ordertype VARCHAR(100));

Table : coffeeconsumers


| FIELD     | TYPE          | NULL | KEY  | DEFAULT | EXTRA          |
|-----------|---------------|------|------|---------|----------------|
| id        | int (11)      | NO   | PRIM | NULL    | auto-increment |
| firstname | varchar (100) | YES  |      | NULL    |                |
| lastname  | varchar (100) | YES  |      | NULL    |                |
| postcode  | varchar (11)  | YES  |      | NULL    |                |
| ordertype | varchar (100) | NO   |      | NULL    |                |


CREATE 2nd TABLE members( ordertype VARCHAR(255), amount INT(3));

Table : consumerorders

| FIELD     | TYPE          | NULL | KEY  | DEFAULT | EXTRA |
|-----------|---------------|------|------|---------|-------|
| ordertype | varchar (255) | YES  | PRIM | NULL    |       |
| amount    | int (3)       | YES  |      | NULL    |       |

#### MySQL command to insert row into tables

insert into coffeeconsumers (id, firstname, lastname,postcode, ordertype) values ("Ian","Fleming", "D28 DF", "beans")

insert into consumerorders (ordertype,amount) values ("beans",100)

#### MySQL join command to join both tables

select coffeeconsumers.id,coffeeconsumers.firstname,consumerorders.ordertype
    -> from consumerorders
    -> INNER JOIN coffeeconsumers on consumerorders.ordertype=coffeeconsumers.ordertype;
