#!/bin/bash


my_array=(A B C D E F G H I J K L M N O P Q R S T U V W X Y Z)
for ((i=0;i<26;i++))
do
    echo ${my_array[$i]}
done
