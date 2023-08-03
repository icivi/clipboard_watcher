import time, datetime
import pyperclip
from PIL import ImageGrab

print('Starting Clipboard Watcher2...')

# Save previous state of clipboard
previous_clipboard_text = pyperclip.paste()  
previous_clipboard_image = ImageGrab.grabclipboard()

while True:
  try:
    # Get current clipboard text and image
    clipboard_text = pyperclip.paste()
    clipboard_image = ImageGrab.grabclipboard()

    if clipboard_text:
      # Check if text has changed
      if clipboard_text!= previous_clipboard_text:
        # Save new text with timestamp
        clip = clipboard_text.replace('\n\n\n', '\n\n')
        clip = clip.replace('\n\n', '\n')
        clip = clip.replace('\n', '')

        # Save new text to file
        with open('clipboard.txt', 'a', encoding='utf-8') as f:
          now = datetime.datetime.now()
          # date_string = now.strftime('%B %d')
          date_string = now.strftime('%H:%M:%S')
          f.write(date_string + ' ' + clip + '\n')
        # Update previous text  
        previous_clipboard_text = clipboard_text

    elif clipboard_image:
      # Check if image has changed
      if clipboard_image and clipboard_image!= previous_clipboard_image:
        # Save new image with timestamp
        now = time.strftime("%Y-%m-%d-%H-%M-%S")
        clipboard_image.save(f'images/clipboard_{now}.png')
        # Update previous image
        previous_clipboard_image = clipboard_image
  except Exception as e:
    print(e)
  # Sleep before next clipboard check
  time.sleep(5)