# Write your MySQL query statement below
select distinct k.num as 'ConsecutiveNums'
from logs k,logs l, logs m
where k.id = l.id - 1 and
      l.id = m.id - 1 and
      k.num = l.num   and
      l.num = m.num
