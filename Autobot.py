import pyautogui
import time
import pyperclip

# Step 1: Click on the icon at (206, 1048)
pyautogui.click(206, 1048)

# Wait for a short period to ensure the application is ready
time.sleep(1)

# Step 2: Click and hold at the start position (686, 211)
pyautogui.moveTo(686, 211)
pyautogui.mouseDown()

# Step 3: Drag to the end position (1829, 915)
pyautogui.moveTo(1829, 915, duration=0.5)
pyautogui.mouseUp()

# Wait for a short period to ensure the text is selected
time.sleep(0.5)

# Step 4: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')

# Wait for the clipboard to update
time.sleep(0.5)

# Step 5: Get the copied text from the clipboard
copied_text = pyperclip.paste()

# Output the copied text to verify (optional)
print("Copied Text:", copied_text)
