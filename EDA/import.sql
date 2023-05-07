-- create a DB for the project 
CREATE DATABASE SQLProjects;

-- create table
CREATE TABLE [dbo].[NewTable] (
    [column_1] INT NULL
);

-- check if connected to the same database
SELECT DB_NAME();

-- if not then use correct DB:
USE SQLProjects;

-- delete table if have to
DROP TABLE dbo.Table;


--- import the .csv
--- if columns base_note and middle_note doesnt import 
--- then use varchar(MAX) since description is too long.
