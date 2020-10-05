import Dnconsole
import Position
import time
import pyautogui


def Lgoin():
    # Dnconsole.Dnconsole.set_screen_size(0)
    Dnconsole.Dnconsole.launch(0)  # 打开模拟器
    time.sleep(15)  # 等待启动

    Dnconsole.Dnconsole.invokeapp(0, 'com.hypergryph.arknights')
    time.sleep(15)  # 等待启动

    pyautogui.click(Position.Login_pos_1[0], Position.Login_pos_1[1], clicks=1, interval=0.0, button='left')  # 网络配置错误确认
    time.sleep(10)
    pyautogui.click(Position.Login_pos_1[0], Position.Login_pos_1[1], clicks=1, interval=0.0, button='left')  # 开始游戏
    time.sleep(25)
    pyautogui.click(Position.Login_pos_1[0], Position.Login_pos_1[1], clicks=1, interval=0.0, button='left')  # 开始唤醒
    time.sleep(25)


def choose_main_stage(macro_stage, micro_stage):
    pyautogui.click(Position.main_stage_pos_start[0], Position.main_stage_pos_start[1],
                    clicks=1, interval=0.0, button='left')  # 选择主线官卡
    time.sleep(3)

    if macro_stage == 1:
        pyautogui.moveTo(125, 175)
        time.sleep(1)
        pyautogui.dragTo(1700, 175, duration=1, button='left')
        time.sleep(1)
        pyautogui.moveTo(125, 175)
        time.sleep(1)
        pyautogui.dragTo(1700, 175, duration=1, button='left')
        time.sleep(1)
        pyautogui.click(Position.macro_stage_1[0], Position.macro_stage_1[1], clicks=1, interval=0.0, button='left')

    time.sleep(3)

    if micro_stage == 7:
        pyautogui.moveTo(1700, 175)
        time.sleep(1)
        pyautogui.dragTo(125, 175, duration=2, button='left')
        time.sleep(3)
        pyautogui.click(Position.micro_stage_7[0], Position.micro_stage_7[1], clicks=1, interval=0.0, button='left')


if __name__ == '__main__':
    Lgoin()

    #time.sleep(5)
    #choose_main_stage(1, 7)

    # dnconsole.Dnconsole.quit(0)  #退出模拟器
