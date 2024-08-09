import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key= "#",

)

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
pyautogui.click(1878, 870)

# Wait for the clipboard to update
time.sleep(0.5)

# Step 5: Get the copied text from the clipboard
copied_text = pyperclip.paste()

# Output the copied text to verify (optional)
print("Copied Text:", copied_text)




# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {"role": "system", "content": "You are a person named chayan who speaks English as well as bangla. You are form Bangladesh and you are a coder. You analiye chat history and respond like chayan. Output should be the next chat resposnce as chayan"},

#     {"role": "user", "content": copied_text}
#   ]
# )

# responce = completion.choices[0].message.content
responce = "I am too much busy now I'll call you letter"


pyperclip.copy(responce)
pyautogui.click(876, 986)
# Wait for a short period to ensure the input field is focused
time.sleep(0.5)

# Step 7: Paste the copied text
pyautogui.hotkey('ctrl', 'v')

# Step 8: Press Enter
pyautogui.press('enter')

# Output the copied text to verify (optional)
print("Copied Text:", copied_text)