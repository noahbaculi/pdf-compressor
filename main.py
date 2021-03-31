## import required libraries
import pyautogui as pyauto
import pandas
from datetime import date
from time import sleep

## Hi darling, I love you

## Condensed guide from https://pyautogui.readthedocs.io/en/latest/quickstart.html
# Left click at (x, y)
# pyauto.click(x, y)
#
# Right click at (x, y)
# pyauto.rightClick(x, y)
#
# Double click at (x, y)
# pyauto.doubleClick(x, y)
#
# Send keyboard text input
# pyauto.typewrite('Hello world!')
#
# Send keyboard single key input
# pyauto.press('enter')
#
# Send hotkey input
# pyauto.hotkey('ctrl', 'c')
#
# Wait for a period of time in seconds
# sleep(1)


pyauto.PAUSE = 2.5  # Pause between ALL pyauto commands in seconds. Keep this long while prototyping and shorten later.
pyauto.FAILSAFE = True  # Failsafe can be triggerd by moving the mouse to the upper-left.

jobs_df = pandas.read_excel('job_details.xlsx', engine='openpyxl')  # read Excel sheet into a dataframe
jobs_df = jobs_df.dropna(axis=0, how='all')  # remove rows with all NaN values
# print(jobs_df)  # preview the dataframe

current_date = date.today().strftime("%B %d, %Y")  # get the current date in text format (ex: March 23, 2021)
# print(current_date)  # preview the date string

# loop through all the jobs (rows of the dataframe)
for index, job in jobs_df.iterrows():
    company = job['Company']
    industry = job['Industry']
    position = job['Position']

    pyauto.click(10, 10)  # click on the template Word cover letter in Finder to select it
    pyauto.hotkey('ctrl', 'c')  # copy the template file
    pyauto.hotkey('ctrl', 'v')  # paste the template file

    pyauto.press('enter')  # start renaming the new file
    pyauto.typewrite(f'Adri Regalado Cover Letter - {company} - {position}')  # rename the new file
    pyauto.press('enter')  # stop renaming the new file

    pyauto.hotkey('ctrl', 'o')  # open the new file
    pyauto.hotkey('ctrl', 'h')  # open the find-replace dialog

    pairs_to_replace = [
        ['[DATE]', date],
        ['[COMPANY]', company],
        ['[INDUSTRY]', industry],
        ['[POSITION]', position]
    ]

    for pair in pairs_to_replace:
        text_to_replace = pair[0]
        replacement = pair[1]
        print(f'{text_to_replace} --> {text_to_replace}')

        # pyauto.press('tab')  # navigate between UI elements
        # pyauto.hotkey('ctrl', 'w')  # close the window



