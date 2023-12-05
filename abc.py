import time
import webbrowser
with open("short.txt") as f:
    for url in f:
        webbrowser.register('opera', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)/Opera/opera.exe"))
        webbrowser.get("opera").open_new_tab(url)
        time.sleep(20)
