Login_pos_1 = [950, 725]
main_stage_pos_start = [1250, 300]

macro_stage_1 = [1000, 500]
micro_stage_7 = [370, 345]

train_pos = [1350, 960]
start_mission_1 = [1350, 950]
start_mission_2 = [1600, 750]


def map_coordinate(coordinate_x_L1, coordinate_x_L2, coordinate_x_R1, coordinate_x_R2,
                   coordinate_y_L1, coordinate_y_L2,
                   x_blocks, y_blocks,
                   target_x, target_y):

    offset_x_1 =(coordinate_x_L2 - coordinate_x_L1) / y_blocks * target_y +coordinate_x_L1
    offset_x_2 = (coordinate_x_R2 - coordinate_x_R1) / y_blocks * target_y +coordinate_x_R1
    coordinate_x=round((offset_x_2-offset_x_1)/x_blocks*(target_x-0.5)+offset_x_1)
    coordinate_y=round((coordinate_y_L2-coordinate_y_L1)/y_blocks*(target_y-0.6)+coordinate_y_L1)
    return coordinate_x,coordinate_y

def operator_choose(operator_count, operator_num):
    operator_x = round(((1825 - 90) / operator_count) * (operator_num - 0.5) + 90)
    operator_y = 950
    return operator_x, operator_y

if __name__ == '__main__':
    coordinate_x, coordinate_y = map_coordinate(coordinate_x_L1=362, coordinate_x_L2=177, coordinate_x_R1=1415,coordinate_x_R2=1560,
                                               coordinate_y_L1=222, coordinate_y_L2=837,
                                               x_blocks=8, y_blocks=5,
                                               target_x=8, target_y=5)
    print(coordinate_x, coordinate_y)
    #print(operator_choose(12,1))