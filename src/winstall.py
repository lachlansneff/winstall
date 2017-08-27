from application import App

apps = [
    App('hyper', 'https://releases.hyper.is/download/win'),
    App('git', 'https://central.github.com/deployments/desktop/desktop/latest/win32'),
    App('atom', 'https://atom.io/download/windows_x64')
]

for i in range(len(apps)):
    apps[i].download()
for i in range(len(apps)):
    apps[i].install()
