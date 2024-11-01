CREATE DATABASE bank;

USE bank;

CREATE TABLE BranchTable(
	"Id" INT NOT NULL AUTO_INCREMENT,
	"Name" VARCHAR(120) NOT NULL,
	"BCode" VARCHAR(15) NOT NULL, 
	"Address" VARCHAR(200) NOT NULL,
	PRIMARY KEY("Id")
);

CREATE TABLE EmployeeTable(
	"Id" INT NOT NULL AUTO_INCREMENT,
	"Name" VARCHAR(50) NOT NULL,
	"Branch" VARCHAR(50) NOT NULL,
	PRIMARY KEY("Id")
);

CREATE TABLE AccountTable (
	"Id" INT NOT NULL AUTO_INCREMENT,
	"Account_Number" VARCHAR(15) NOT NULL,
	"Account_Type" VARCHAR(15) NOT NULL,
	"BCode" VARCHAR(15) NOT NULL,
	"Name" VARCHAR(50) NOT NULL,
	"Gender" VARCHAR(10) NOT NULL,
	"DOB" Date,

	"Address" VARCHAR(50) NOT NULL,
	"Aadhar" VARCHAR(12) NOT NULL,
	"Balance" double NOT NULL,

	PRIMARY KEY ("Id")
);


CREATE TABLE TransactionTable( 
	"Id" INT NOT NULL AUTO_INCREMENT,

	"Date" Date NOT NULL,
	"Account_Num" Varchar(15),
	"Transaction_Type" Varchar(15),   
	"Amount" double,
	PRIMARY KEY ("Id")
);
 

CREATE TABLE ServiceTable( 
	"Date" Date NOT NULL,
	"Account_Num" Varchar(15),
	"ServiceName" Varchar(100), 
	"Description" Varchar(200), 
	"Amount" double,
	"TransactionId" INT NOT NULL,
	INDEX par_ind (TransactionId),
	CONSTRAINT fk_tranTable FOREIGN KEY (TransactionId)
		REFERENCES TransactionTable (Id)
			ON DELETE CASCADE
			ON UPDATE CASCADE
) ENGINE=INNODB;


// truncate table which has foreign key contraints.

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE ServiceTable;
SET FOREIGN_KEY_CHECKS = 1;

// 