str=com.yy.test.boardcast

echo ${str#*.}  

echo ${str##*.}  

echo ${str%.*}  

echo ${str%%.*} 


str2=origin/release/2.0.2_maint
echo ${str2#*\/}

echo ${str2/origin\/}


