first_x=879
first_y=2365

second_x=1075
second_y=2283

third_x=1281
third_y=2156

location_1=(420 1800)
location_2=(733 1642)
location_3=(1070 1471)
location_4=(405 1440)
location_5=(752 1298)
location_6=(1085 1117)
location_7=(395 1113)
location_8=(740 979)
location_9=(1065 773)

upgrade_all_position=(1285 1768)
upgrade_position=(1178 2745)

upgrade=10

while true
do
    input swipe ${location_1[@]} ${location_3[@]} 150
    input swipe ${location_4[@]} ${location_6[@]} 150
    input swipe ${location_7[@]} ${location_9[@]} 150
    
    upgrade=$(($upgrade-1))
    
    echo $(($upgrade))

    collect=4
    
    function collect_first () {
        input swipe $first_x $first_y 282 1739 90
        input swipe $first_x $first_y 735 1455 90
        input swipe $first_x $first_y 1071 1326 90
        input swipe $first_x $first_y 369 1286 90
        input swipe $first_x $first_y 753 1105 90
        input swipe $first_x $first_y 1069 943 90
        input swipe $first_x $first_y 350 865 90
        input swipe $first_x $first_y 641 674 90
        input swipe $first_x $first_y 1042 388 90
    }

    function collect_second () {
        input swipe $second_x $second_y 282 1739 90
        input swipe $second_x $second_y 695 1455 90
        input swipe $second_x $second_y 1071 1326 90
        input swipe $second_x $second_y 309 1286 90
        input swipe $second_x $second_y 753 1105 90
        input swipe $second_x $second_y 1069 943 90
        input swipe $second_x $second_y 320 865 90
        input swipe $second_x $second_y 641 674 90
        input swipe $second_x $second_y 1042 388 90
	}

    function collect_third () {
        input swipe $third_x $third_y 282 1739 90
        input swipe $third_x $third_y 635 1455 90
        input swipe $third_x $third_y 1071 1326 90
        input swipe $third_x $third_y 289 1286 90
        input swipe $third_x $third_y 703 1105 90
        input swipe $third_x $third_y 1069 943 90
        input swipe $third_x $third_y 270 805 90
        input swipe $third_x $third_y 641 674 90
        input swipe $third_x $third_y 1042 388 90
	}
 
    function upgrade_all () {
        input tap ${upgrade_all_position[@]}
        input tap ${location_1[@]}
        input tap ${upgrade_position[@]}
        input tap ${location_2[@]}
        input tap ${upgrade_position[@]}
        input tap ${location_3[@]}
        input tap ${upgrade_position[@]}
        input tap ${location_4[@]}
        input tap ${upgrade_position[@]}
        input tap ${location_5[@]}
        input tap ${upgrade_position[@]}
        input tap ${location_6[@]}
        input tap ${upgrade_position[@]}
        input tap ${location_7[@]}
        input tap ${upgrade_position[@]}
        input tap ${location_8[@]}
        input tap ${upgrade_position[@]}
        input tap ${location_9[@]}
        input tap ${upgrade_position[@]}
        input tap ${upgrade_all_position[@]}
    }

    while [ $collect -gt 1 ]
    do
        collect_first
        collect_second
        collect_third
        collect=$(($collect-1))
    done

    if [ $upgrade -eq 1 ]; then
        upgrade_all
        upgrade=10
    fi
    
    input tap 720 2500
    sleep 1
    
done
