@ECHO OFF
Setlocal EnableDelayedExpansion


SET temp_str=videoengine-vs2015
echo %temp_str% | findstr /r "[a-z]-vs[0-9]">nul 2>&1
if errorlevel 1 (
  ECHO does not contain
  SET REPO_OUTPUT_NAME=videoengine
) else (
  ECHO contains
  ECHO %temp_str%
  SET vs_version=%temp_str:~-4%
  echo 截取的字符串为:!vs_version!
  SET REPO_OUTPUT_NAME=videoengine!vs_version!
)

  echo %REPO_OUTPUT_NAME%
