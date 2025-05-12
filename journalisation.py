import win32gui
import time
from datetime import datetime
import requests

def get_window_tittle():
    hwnd = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(hwnd).strip()

def send_log_to_server(log_file="fenetre.log", url="http://localhost/serveur_python/log.php"):
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            log_contenu = f.read()
        if log_contenu.strip():
            reponse = requests.post(url, data={"log": log_contenu})
            print("Reponse du serveur :", reponse.status_code)
            if reponse.status_code == 200:
                open(log_file, "w", encoding="utf-8").close() 
    except Exception as e:
        print(f"Erreur d'envoi : {e}")

def format_duration(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def log_windows(interval=5, log_file="fenetre.log"):
    last_title = ""
    start_time = time.time()
    try:
        while True:
            title = get_window_tittle()
            if title and title != last_title:
                now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                if last_title:
                    duration = time.time() - start_time
                    duree_str = format_duration(duration)
                    log_line = f"{now} Fenetre active : {title} (temps: {duree_str})\n"
                else:
                    log_line = f"{now} Fenetre active : {title}\n"
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_line)
                print(log_line.strip())
                send_log_to_server(log_file)
                last_title = title
                start_time = time.time()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nArrêt de la journalisation.")

if __name__ == "__main__":
    log_windows(interval=2)