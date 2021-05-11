# Created by MagneticEnder. https://github.com/MagneticEnder/Discord-Spammer
import pyautogui
import time

# These are the tags that will be automatically spammed.
# You can add as many as you want, just be sure to include them later.
tag1 = '@everyone '
tag2 = ' @here'

# This part of the script grabs your inputs.
msg = input("Enter the message you want to spam...")
n = input("Enter the amount of times to spam the message...")
interval = input("Enter the delay in seconds between each message...")
print("")
time.sleep(1)

# This part counts down.
print ("The spam will begin in 10...")
time.sleep(1)
for i in range(9):
    print(str(9 - i) + "...")
    print("")
    time.sleep(1)

# This is the spamming part. It writes the tags, your message, and triggers the RETURN key.
for i in range(0, int(n)):
    pyautogui.typewrite(tag1 + msg + tag2 + '\n')
    time.sleep(int(interval))

input("Completed the specified task. Press any key to exit.")
