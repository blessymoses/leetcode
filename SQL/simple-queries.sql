select e.Id, e.Name, e.ManagedBy from Employees e join Managers m
on m.Id = e.ManagedBy
where m.Name="Sandy Kim";

select * from Employees 
where ManagedBy is null;