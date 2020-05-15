Setlocal EnableDelayedExpansion


set TAG_NAME=OPENSLL-ANDROID_2.5.0_REL
set RELEASE_VERSION=2.4.0

set var=!TAG_NAME:%RELEASE_VERSION%=!
echo "check %TAG_NAME%: remove %RELEASE_VERSION%, get %var%"

if %var% == %TAG_NAME% (
    echo "check failed,build %TAG_NAME% error, Please contact the administrator!"
    exit 1
)

echo "******check pass[%RELEASEBUILD%],build %TAG_NAME% start******"

