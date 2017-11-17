
str="apple, tree, apple tree"
echo ${str/apple/APPLE}   # 替换第一次出现的apple
echo ${str//apple/APPLE}  # 替换所有apple

echo ${str/#apple/APPLE}  # 如果字符串str以apple开头，则用APPLE替换它
echo ${str/%apple/APPLE}  # 如果字符串str以apple结尾，则用APPLE替换它

profile="AppStore_9f26ac1d-86af-4358-8467-a46c0df336d3_com.ysl.oneapple.mobileprovision"
uuid="9f26ac1d-86af-4358-8467-a46c0df336d3"
echo ${profile/_$uuid/}
