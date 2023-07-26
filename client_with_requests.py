import requests
import tkinter as tk
from tkinter import filedialog

url = "http://127.0.0.1:8000/caps/upload"


def choose_file(url):
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                           filetypes=(("Capture Files", "*.pcap"), ("All Files", "*.*")))
    if file_path:
        upload_file(url, file_path)


def upload_file(url, file_path):
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f, 'application/octet-stream')}
            print(files)
            response = requests.post(url, files=files)
        if response.status_code == 200:
            print("File uploaded successfully.")
            return response.json()
        else:
            print("Failed to upload the file. Response status code:", response.status_code)

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

# if __name__ == "__main__":
# file_path = r'C:\Users\ימין\Music\לימודים\python_ele\קבצים של הפרויקט גמר\קבצי pcap\evidence02.pcap'
#
# try:
#     response_data = upload_pcap_file(url, file_path)
#     print("Response:", response_data)
# except requests.exceptions.RequestException as e:
#     print("Error occurred during upload:", e)
