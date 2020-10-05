import Position
import time
import pyautogui
import pandas as pd
import pytesseract.pytesseract
import tesseract

# script_df = pd.read_excel(r'C:\Users\Administrator\PycharmProjects\Arknight_steptool\游戏脚本.xlsx')
time.sleep(3)
ocr_cost_flag = 1

pyautogui.click(Position.train_pos[0], Position.train_pos[1], clicks=1, interval=0.0, button='left')
time.sleep(3)
#pyautogui.click(Position.start_mission_1[0], Position.start_mission_1[1], clicks=1, interval=0.0, button='left')
#time.sleep(3)
pyautogui.click(Position.start_mission_2[0], Position.start_mission_2[1], clicks=1, interval=0.0, button='left')
time.sleep(3)


while ocr_cost_flag == 1:
    cost_img = pyautogui.screenshot(region=(1735, 720, 70, 65))  # ocr_box
    cost_img.save('cost_img.png')

    cost_img_correct = tesseract.IMG_correct('cost_img.png')
    cost = pytesseract.image_to_string(cost_img_correct,
                                       lang='eng',
                                       config='tessedit_char_whitelist=0123456789 -psm 6 digits'
                                       )

    if cost.strip().isdigit() == True:
        cost = int(cost)
        print(cost)

        if cost >= 20:
            pyautogui.press('f')
            ocr_cost_flag = 0

        time.sleep(0.5)
