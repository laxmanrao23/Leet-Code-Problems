# Write your MySQL query statement below
select a.name as Employee from Employee as a
join Employee as b
on a.ManagerId = b.id and a.salary > b.salary;