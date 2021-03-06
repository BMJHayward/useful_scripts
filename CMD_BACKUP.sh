:: Backup args:
::   /V Verify? (yes/no)
::   /R Restrict access to owner? (yes/no)
::   /RS Removable storage? (yes/no)
::   /HC Hardware compression (on/off)
::   /M Backup type (normal/copy/differential/incremental/daily)
::   /L Log file type (f/s/n)
::   /D "Description"
::   /J "Job-name"
::   /F "File-name"

SETLOCAL

:: ensure that network drives are mounted
CALL C:\bat\configs\MapShares-home.cmd
echo on

set today=%DATE:~0,3%
if %today%==Mon set yesterday=0Sunday
if %today%==Tue set yesterday=1Monday
if %today%==Wed set yesterday=2Tuesday
if %today%==Thu set yesterday=3Wednesday
if %today%==Fri set yesterday=4Thursday
if %today%==Sat set yesterday=5Friday
if %today%==Sun set yesterday=6Saturday

set configsDir=%~dp0
set storePath=C:\mybackups

:: (eg: Monday C files)
set title=%yesterday% backup set


echo %DATE% %TIME% %title% > "%storePath%\%yesterday%_backup.log"

CALL BackupConfigs.bat

:: Create new BKF file
call C:\WINDOWS\system32\ntbackup.exe backup ^
    "@%configsDir%\daily.bks" ^
    /V:yes /R:no /RS:no /HC:off /M normal /L:s ^
    /D "%title%" ^
    /J "%title%.job" ^
    /F "%storePath%\%yesterday%.bkf" ^
    >> "%storePath%\%yesterday%_backup.log"

echo %DATE% %TIME% Completed >> "%storePath%\%yesterday%_backup.log"

copy "%storePath%\%yesterday%.bkf" "V:\Backups\NEPTUNE"

CALL C:\bat\clean-temps.bat

defrag -v C: > "%storePath%\%yesterday%_defrag.log"

:: display backup directories
start /D"C:\bat\Backups\" checkbkf.bat

ENDLOCAL

::pause