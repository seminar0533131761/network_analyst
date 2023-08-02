import tkinter as tk
from tkinter import filedialog

import requests

url = "http://127.0.0.1:8000/caps/upload"


# note:  this file is not in use yet because we are using postman for uploading files
def choose_file(url):
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Capture Files", "*.pcap"), ("All Files", "*.*")))
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Capture Files", "*.pcap;*.cap;*.pcapng"), ("All Files", "*.*")))

    if file_path:
        upload_file(url, file_path)


def upload_file(url, file_path):
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, 'application/octet-stream')}
            response = requests.post(url, files=files)
        if response.status_code == 200:
            return response.json()

    except Exception as e:
        print("Error occurred while uploading the file:", e)


choose_file(url)
# Create the GUI window
window = tk.Tk()
window.title("File Upload")

# Create a button to choose the file
choose_button = tk.Button(window, text="Choose File To Process", command=choose_file, padx=30, pady=30)
choose_button.pack(pady=80, padx=80)

# Run the GUI event loop
window.mainloop()
