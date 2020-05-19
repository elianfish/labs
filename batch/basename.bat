

set DEV_LINE=origin/maint/test/2.7.1_feature
for %%f in (%DEV_LINE%) do set brname=%%~nxf
echo %brname%
