import requests
from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO

def close_window(event=None):
    window.destroy()  # Close the Tkinter window

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"sk-ht0xT3BQMMuesKhCeKBAHigToeqLpkYjSmHyEHdgQ0P9F40i",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "a cartoon bear eating peanut butter",
        "output_format": "webp",
    },
)

if response.status_code == 200:
    image_data = response.content
    image = Image.open(BytesIO(image_data))

    # Create a Tkinter window
    window = tk.Tk()
    window.attributes("-fullscreen", True)  # Set the window to full-screen
    window.configure(bg='black')  # Optional: Set background color to black

    # Convert image to Tkinter-compatible format
    photo = ImageTk.PhotoImage(image)

    # Create a label widget to hold the image
    label = tk.Label(window, image=photo, bg='black')
    label.pack(fill="both", expand=True)  # Fill the entire window

    # Bind the Escape key to close the window
    window.bind('<Escape>', close_window)

    window.mainloop()
else:
    raise Exception(str(response.json()))