REM 
REM DO NOT TRY TO GENERATE THE SIS FILE IF YOUR PATH CONTAINS SPACES.
REM ENSYMBLE DOES NOT SUPPORT THEM ! COPY THIS PROJECT TO C:\
REM BEFORE RUNNING THIS SCRIPT.
REM
@echo off

SET PYTHON=C:\Python25\python.exe
SET APPNAME=Medcalc
SET CAPBLS=LocalServices+ReadUserData+WriteUserData+UserEnvironment
SET SRCDIR=src
SET TMPDIR=src.tmp
SET ICON=%SRCDIR%\logo2.svg
SET MEDCALCVER=0.6.0

REM Path to module-repo, inside Python For S60
SET PYS60DIR=C:\Arquivos de programas\PythonForS60

SET OPTS=--verbose --version="%MEDCALCVER%" --appname="%APPNAME%" --textfile=disclaimer.txt ^
         --extrasdir=extras --heapsize=4k,5M --caps=%CAPBLS% --icon="%ICON%"

echo "Populating temp dir"
if exist "%TMPDIR%" rmdir /s /q "%TMPDIR%"
mkdir %TMPDIR%\extras\data\python\medcalc

copy  %SRCDIR%\lib\               %TMPDIR%\extras\data\python\medcalc\
copy  %SRCDIR%\img\               %TMPDIR%\extras\data\python\medcalc\
copy  %SRCDIR%\default.py         %TMPDIR%\

if not exist .\module-repo\ xcopy /E "%PYS60DIR%\module-repo" .\module-repo\
if not exist .\templates\   xcopy /E "%PYS60DIR%\templates"   .\templates\
if not exist ensymble.py    xcopy /E "%PYS60DIR%\ensymble.py" .
if not exist openssl.exe    xcopy /E "%PYS60DIR%\openssl.exe" .

%PYTHON% ensymble.py py2sis %OPTS% "%TMPDIR%" "%APPNAME%-%MEDCALCVER%.sis"

