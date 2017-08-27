from application import App
from feature import Feature

apps = [
    App('hyper', 'https://releases.hyper.is/download/win'),
    App('git', 'https://central.github.com/deployments/desktop/desktop/latest/win32'),
    App('atom', 'https://atom.io/download/windows_x64'),
    App('python3', 'https://www.python.org/ftp/python/3.6.2/python-3.6.2.exe', '/quiet PrependPath=1'),
    Feature('Microsoft-Windows-Subsystem-Linux')
]

for i in range(len(apps)):
    if app[i].download:
        apps[i].download()
for i in range(len(apps)):
    apps[i].install()
