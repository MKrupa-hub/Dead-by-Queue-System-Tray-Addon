# Dead-by-Queue-System-Tray-Addon
A simple system tray addon that shows the estimated killer queue time in Dead by Daylight. This project uses data provided by https://www.deadbyqueue.com



Prerequisuites:
- Python 3.9+ (works with Miniconda but you can also use: Anaconda, python.org official installer)

Steps:
1. Key Windows + r than type shell:startup
2. Right click -> new Shortcut
3. Paste path in template "path to pythonw" "path to this python script" for example "C:/Users/mateu/miniconda3/pythonw.exe" "C:\Users\mateu\PycharmProjects\PythonProject\killerQueue.pyw"
4. To test, double-click the shortcut and check if the icon appears in the system tray.
5. Enjoy!

<img width="125" height="112" alt="image" src="https://github.com/user-attachments/assets/58cabf96-418e-461d-a76d-a3e5d1ef8e1d" />

IMPORTANT!!!
Script uses eu-central-1 region please check which region you are playing and update below in script according to https://www.deadbyqueue.com site. 
```python
API_URL = "https://api.deadbyqueue.com/queuetime?region=eu-central-1"
```
In order to get needed url click on dbq site "Check the queue times from your Twitch chat" -> Moobot" -> select region -> copy url 




