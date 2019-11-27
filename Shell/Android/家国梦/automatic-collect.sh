first_x=453
first_y=1080

second_x=550
second_y=1052

third_x=660
third_y=979

location_1=(198 808)
location_2=(360 712)
location_3=(538 639)
location_4=(194 640)
location_5=(365 549)
location_6=(531 464)
location_7=(190 457)
location_8=(380 388)
location_9=(542 279)

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