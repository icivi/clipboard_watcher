import time, datetime
import pyperclip
from PIL import ImageGrab

print('Starting Clipboard Watcher...')

# Save previous state of clipboard
previous_clipboard_text = pyperclip.paste()  
previous_clipboard_image = ImageGrab.grabclipboard()

while True:
  # Get current clipboard text and image
  clipboard_text = pyperclip.paste()
  clipboard_image = ImageGrab.grabclipboard()

  if clipboard_text:
    # Check if text has changed
    if clipboard_text != previous_clipboard_text:
      # Save new text to file
      with open('clipboard.txt', 'a', encoding='utf-8') as f:
        now = datetime.datetime.now()
        date_string = now.strftime('%B %d')
        f.write('\n' + date_string + '\n' + clipboard_text + '\n')
      # Update previous text  
      previous_clipboard_text = clipboard_text

  else:
    # Check if image has changed
    if clipboard_image and clipboard_image != previous_clipboard_image:
      # Save new image with timestamp
      now = time.strftime("%Y-%m-%d-%H-%M-%S")
      clipboard_image.save(f'images/clipboard_{now}.png')
      # Update previous image
      previous_clipboard_image = clipboard_image

  # Sleep before next clipboard check
  time.sleep(5)