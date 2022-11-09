# Write your MySQL query statement below
SELECT email
From Person
Group BY email
Having Count(*) > 1