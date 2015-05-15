BACKUP log [myDatabase] with truncate_only
go
DBCC SHRINKDATABASE ([myDatabase], 10, TRUNCATEONLY)
go

BACKUP
LOG [myDatabase] TO DISK = N'C:\Backups\myDatabase_log.trn' WITH
NOFORMAT, NOINIT, NAME = N'myDatabase_log', SKIP, REWIND, NOUNLOAD,
STATS = 10