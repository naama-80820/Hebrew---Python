@echo off

setlocal enabledelayedexpansion

:run_python
set /p file1=Enter input file: 
set /p file2=Enter output file: 
set SCRIPT_DIR=%~dp0
cd %SCRIPT_DIR%
python __main__.py %file1% %file2%

if %errorlevel% neq 0 (
    echo An error occurred.
) else (
    echo The script ran successfully.
)

set /p choice=Press 'c' to continue or 'q' to quit: 
if "!choice!" equ "c" (
    goto :run_python
) else (
    pause
    exit
)
