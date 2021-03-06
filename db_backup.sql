DECLARE @currentday varchar(10)
set @currentday = datepart(day,getdate())
IF LEN(@currentday) = 1
BEGIN
    SET @currentday = '0' + @currentday
END
DECLARE @currentmonth varchar(10)
SET @currentmonth = datepart(month,getdate())
IF LEN(@currentmonth) = 1
BEGIN
    SET @currentmonth = '0' + @currentmonth
END
DECLARE @currentyear varchar(10)
SET @currentyear = datepart(year,getdate())
DECLARE @fileName varchar(100)
SET @fileName = 'c:\Backups\Database\myDatabase_' + @currentyear
+ '_'    + @currentmonth  + '_' + @currentday  + '.bak'
BACKUP DATABASE myDatabase TO DISK = @fileName WITH NOFORMAT, INIT,
NAME = N'myDatabase -Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
GO