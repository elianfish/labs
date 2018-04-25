@echo off


for /f "tokens=5,6 delims=/\" %%a in ("%TEST_VERSION_PATH%") do (
    set c5_platform=%%a
    set c6_pdtname=%%b
)

echo %c5_platform%  %c6_pdtname%
set APP_NAME=%c6_pdtname%-%c5_platform%
echo APP_NAME=%APP_NAME%

echo APP_NAME=%APP_NAME% > %JOB_NAME%.properties
