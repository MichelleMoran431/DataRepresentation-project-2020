## Data-Representation Project 2020
## Student : Michelle Moran

Introduction : 

The assessment choosen is the Web Application project A - To create a basic flask server that has a REST API, to preform CRUD operations. To create one database table and have an accompanying web interface, using AJAX calls, to perform these CRUD operations.

A GIT-HUB file was created and the link was submitted  ( reference : https://github.com/g00387856/DataRepresentation-project-2020)

The following files : server.py and CoffeeExpertsDAO.py use CRUD operations for updates to the server and database.

**File index :


|        FILE NAME        |                                               DESCRIPTION                                                |
|:-----------------------:|:--------------------------------------------------------------------------------------------------------:|
| initdb.sql              | An outline of the two database tables created : coffeeconsumers and consumerorders                       |
| /gitignore/config.py    | configuration code - stored here so it will not be push up to github                                     |
| DBconfigtemplate.py     | Template of config code for future reference.                                                            |
| requirements.md         | Outlines details of how to run this project                                                              |
| ReadMe.md               | Project Details                                                                                          |
| server.py               | Web server for local host                                                                                |
| CoffeeexpertsDAO.py     | Data Access Object file for interacting with the coffeeconsumers database                                |
| CoffeeExperts Orders.py | Testing database connection                                                                              |
| /staticpages/index.html | In staticpages folder - Home page that will facilitate the update/creation/deletion of consumer details  |

**1. Initdb.sql 

This file shows the two database tables that were created in MySQL. 


### MySQL Database : coffeeexpress
----------------------------------

Reference Materia:

 - https://www.w3schools.com

Reference file  : initdb.sql - outlines how the two tables were created in MYSQL. The tables create were :


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
    
 ###**Configuration files 
 
 Reference material # DR 10.01 Configuration files : Andrew Beatty ( week 10 material on Moodle)
 
These were created to cover if this code is ran on different machines. The gitignore file was created to store any file that has config in its name so that it will not be uploaded to github preventing future issues. A template of this file was created so that we would have a copy.

  - /gitignore/config.py    |
  - DBconfigtemplate.py  
  
  The method used is storing in a python file as a variable and then it was imported into another file
   
### Project Server

-------------------------

FIle Reference : Server.py

This program creates a Flask server , which allows the database to interact with a web based interface. 
The following was imported. 

from flask import Flask, jsonify, request, abort,url_for,redirect
from CoffeeExpertsDAO import coffeedao  - a link to the database created in CoffeeExpertsDAO.py below

Run the server in an anaconda base command prompt. - python server.py


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
<td>/coffeeconsumers</td>
<td>none</td>
<td>[{...},{...},{...}]</td>  
</tr>
<tr>
<td>Find by id</td>
<td>GET</td>
<td>/coffeeconsumers/id</td>
<td>none</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode":"xxx"}]
</td> 
<tr>
<td>Create</td>
<td>POST</td>
<td>/coffeeconsumers</td>
<td>{"Firstname":"xxx"},{"Lastname":"xxx","Postcode:"xxx"}</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode":"xxx"}]
</td>
</tr>
<tr>
<td>Update</td>
<td>PUT</td>
<td>/coffeeconsumers/id</td>
<td>{"Postcode:"xxx"}</td>
<td>[{"id":"1","Firstname":"xxx"},{"Lastname":"xxx","Postcode:"xxx"}]
</td>
</tr>
<td>Delete</td>
<td>DELETE</td>
<td>/coffeeconsumers/id</td>
<td>none</td>
<td>{"done:"true}
</td>
</tr>  
</tbody>
</table>

###**CoffeeExpertsDAO.py 
-------------------

Reference material : DR.9.4 DAO Walkthrough Andrew Beatty

This file is the link between the database and the flask server. 
A Class is created called coffeedao which contains all the functions needed for interaction with the database.

**def init **- links to the database
** def create -create a new record, into the database throught the sql statement INSERT. The values are stated here also. Curser is used to carryout the function to the database. it is imported at the start of the program code. 
**def getAll** - returns all the data from the database
**def ConvertToDict** - converts the returned data (a tupple) from the database into a dictionary object called 'coffeeconsumers{}'. The program iterates through the results, and for every column name returned, it converts it to a array.
**def findByID** - searches the database for a specific id number, and returns to the user.
**def update** - code to update an existing record in the database
**def delete** - code to allow a user to delete an existing record in a database.

###**/staticpages/index.html
--------------------------

Reference Material : 

 - DR9.6 and DR9.7 HTML-AJAX Walkthrough parts - Andrew Beatty
 - https://www.w3schools.com/html/
 - https://www.w3schools.com/bootstrap/

Creating the html that will use AJAX to link to the server and provide a user interface: 

It has two screens : 

 - Table displaying all the coffee consumers
 - Create/Edit/Update screen
 
It was coded and html created. Following Andrew Beattys walkthrough lectures , the getall , create and delete and then update completed. 
Using Bootstrap to style the user interface , following www.w3schools.com tutorials. 


 








