SELECT  * FROM SCOTT.EMP;
SELECT ENAME, sal FROM scott.emp;

SELECT * 
FROM scott.emp
WHERE Ename = 'BLAKE'
    
SELECT * 
FROM scott.emp
WHERE SAL > 2000 AND JOB LIKE 'M%'
    
SELECT * 
FROM scott.dept
WHERE DEPTNO = 30 

-- añadimos parte de una tabla igual a otra    
SELECT * 
FROM scott.emp
INNER JOIN scott.dept ON emp.deptno = dept.deptno

SELECT nombre, apellido, emp.nombre, dept.nombre --filtrado de columnas 
FROM scott.emp
INNER JOIN scott.dept ON emp.deptno = dept.deptno
where
order by nombre desc --ordenar en columnas, en este caso 1 y es por nombre en orden alfabetico
--1
SELECT * 
FROM scott.emp
INNER JOIN scott.dept ON emp.deptno = dept.deptno
WHERE DNAME = 'RESEARCH'

--2
SELECT * 
FROM scott.emp
WHERE EMPNO = 7844
--3
SELECT * 
FROM scott.emp
INNER JOIN scott.dept ON emp.deptno = dept.deptno
WHERE JOB  = 'MANAGER' AND LOC = 'CHICAGO'
--4
SELECT ENAME, SAL, LOC
FROM scott.emp
INNER JOIN scott.dept ON emp.deptno = dept.deptno
WHERE LOC = 'NEW YORK'
ORDER BY SAL DESC
--5
SELECT ENAME, SAL, LOC
FROM scott.emp
INNER JOIN scott.dept ON emp.deptno = dept.deptno
WHERE LOC = 'NEW YORK' AND SAL > 2000
ORDER BY SAL DESC
LIMIT 10
--SELECT * cuando utilizamos el * sacamos la informacion de todas las columnas, si queremos desaturar 
--escribimos el nombre de la columna que queremos sacar como SAL = salario
