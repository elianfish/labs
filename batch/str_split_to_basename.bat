@echo off

set BRANCHNAME_IN=orgin/dev/elianfish/111_2.0.9_1011_feature
set BRANCHNAME_OUT=DEFAULT_ERROR
call:basename %BRANCHNAME_IN% %BRANCHNAME_OUT%

echo.BRANCHNAME_IN : %BRANCHNAME_IN%
echo.BRANCHNAME_OUT: %BRANCHNAME_OUT%

::basename 函数
::用法 call:basename %入参% %BRANCHNAME_OUT%
::入参的值不会被修改，调用函数后使用BRANCHNAME_OUT的值
:basename
set str=%1
:loop
for /f "tokens=1* delims=/" %%a in ("%str%") do (
  set str=%%b
  set BRANCHNAME_OUT=%str%
)
if defined str goto :loop
goto:eof
