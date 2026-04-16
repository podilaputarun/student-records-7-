CREATE DATABASE university_db;

USE university_db;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE marks (
    student_id INT,
    subject VARCHAR(50),
    marks INT
);
select * from students;