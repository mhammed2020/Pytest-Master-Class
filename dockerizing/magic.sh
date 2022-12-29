#!/bin/bash

# PMA
counter=${MY_COUNTER}
msg=${MY_MSG}
for n in $(seq $counter)
do 
    echo "$n: $msg"
    sleep 1 
done 
