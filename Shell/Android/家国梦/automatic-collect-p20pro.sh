first_x=667
first_y=1848

second_x=829
second_y=1793

third_x=965
third_y=1692

location_1=(292 1741)
location_2=(548 1350)
location_3=(780 1228)
location_4=(294 1233)
location_5=(538 1082)
location_6=(801 986)
location_7=(303 957)
location_8=(548 855)
location_9=(805 728)

while true
do
    input swipe ${location_1[@]} ${location_3[@]}
    input swipe ${location_4[@]} ${location_6[@]}
    input swipe ${location_7[@]} ${location_9[@]}
    
    collect=4

    function collect_first () {
        input swipe $first_x $first_y ${location_1[@]} 90
        input swipe $first_x $first_y ${location_2[@]} 90
        input swipe $first_x $first_y ${location_3[@]} 90
        input swipe $first_x $first_y ${location_4[@]} 90
        input swipe $first_x $first_y ${location_5[@]} 90
        input swipe $first_x $first_y ${location_6[@]} 90
        input swipe $first_x $first_y ${location_7[@]} 100
        input swipe $first_x $first_y ${location_8[@]} 100
		input swipe $first_x $first_y ${location_9[@]} 100
    }

    function collect_second () {
        input swipe $second_x $second_y ${location_1[@]}  90 
        input swipe $second_x $second_y ${location_2[@]}  90 
        input swipe $second_x $second_y ${location_3[@]}  90 
        input swipe $second_x $second_y ${location_4[@]}  90 
        input swipe $second_x $second_y ${location_5[@]}  90 
        input swipe $second_x $second_y ${location_6[@]}  90 
        input swipe $second_x $second_y ${location_7[@]}  100 
        input swipe $second_x $second_y ${location_8[@]}  100 
        input swipe $second_x $second_y ${location_9[@]}  100
	}

    function collect_third () {
        input swipe $third_x $third_y ${location_1[@]}  90
        input swipe $third_x $third_y ${location_2[@]}  90
        input swipe $third_x $third_y ${location_3[@]}  90
        input swipe $third_x $third_y ${location_4[@]}  90
        input swipe $third_x $third_y ${location_5[@]}  90
        input swipe $third_x $third_y ${location_6[@]}  90
        input swipe $third_x $third_y ${location_7[@]}  100
        input swipe $third_x $third_y ${location_8[@]}  100
        input swipe $third_x $third_y ${location_9[@]}  100
	}

    while [ $collect -gt 1 ]
    do
        collect_first
        collect_second
        collect_third
        collect=$(($collect-1))
    done


    input tap 385 914
    sleep 5
done
