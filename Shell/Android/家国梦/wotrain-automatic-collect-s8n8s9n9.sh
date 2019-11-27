location_1=(420 1900)
location_2=(733 1742)
location_3=(1070 1571)
location_4=(405 1540)
location_5=(752 1398)
location_6=(1085 1217)
location_7=(395 1213)
location_8=(740 1079)
location_9=(1065 873)

upgrade_all_position=(1285 1768)
upgrade_position=(1178 2745)

upgrade=30

while true
do
    input swipe ${location_1[@]} ${location_3[@]}
    input swipe ${location_4[@]} ${location_6[@]}
    sleep 1
    input swipe ${location_1[@]} ${location_3[@]}
    sleep 1
    input swipe ${location_1[@]} ${location_3[@]}
    input swipe ${location_4[@]} ${location_6[@]}
    sleep 1
    input swipe ${location_1[@]} ${location_3[@]}
    sleep 1
    input swipe ${location_1[@]} ${location_3[@]}
    input swipe ${location_7[@]} ${location_9[@]}

    upgrade=$(($upgrade-1))
    
    echo $(($upgrade))
    
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

    if [ $upgrade -eq 1 ]; then
        upgrade_all
        upgrade=30
    fi
    
    input tap 720 2500
    sleep 1
    
done
