-- Active: 1746729928632@@127.0.0.1@5432@xlsx_to_sql
CREATE TABLE students(
    student_id VARCHAR(9) PRIMARY KEY,
    username VARCHAR(50),
    fullname VARCHAR(60)
)


CREATE TABLE problems(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    judge_score INTEGER,
    final_score INTEGER
)   student_id VARCHAR(9) REFERENCES students(student_id)