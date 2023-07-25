import requests


def upload_pcap_file(url, file_path):
    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f, 'application/octet-stream')}
        print(files)
        response = requests.post(url, files=files)
        return response.json()


if __name__ == "__main__":
    url = "http://127.0.0.1:8000/caps/upload"
    file_path = r'C:\Users\OWNER\Downloads\evidence01.pcap'

    try:
        response_data = upload_pcap_file(url, file_path)
        print("Response:", response_data)
    except requests.exceptions.RequestException as e:
        print("Error occurred during upload:", e)
