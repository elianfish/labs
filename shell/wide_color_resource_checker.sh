targetDir=${TARGET_BUILD_DIR}
echo "targetDir:$targetDir"
for file in `find $targetDir -name 'Assets.car'`
do
	check_result=$(assetutil --info $file | grep -A 5 -B 16 '"DisplayGamut" : "P3"')
	if [ "$check_result" != "" ]
	then
		echo "$file has P3 error $check_result"
		exit 1
	else
		echo "$file check OK"
	fi
done
