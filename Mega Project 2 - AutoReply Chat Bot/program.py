import pyautogui
import pyperclip
import time

# Wait a few seconds to allow user to switch to correct screen
time.sleep(3)

# Step 1: Click on the icon
pyautogui.click(985, 1050)
time.sleep(1)

# Step 2: Select the text by dragging from (553, 139) to (1899, 948)
pyautogui.moveTo(553,139)
pyautogui.dragTo(1899, 948, duration=2.0, button='left')
time.sleep(0.5)


# Step 3: Copy to clipboard using Ctrl+C
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get clipboard contents
text_copied = pyperclip.paste()

# Display or use the variable
print("Copied Text:\n", text_copied)
