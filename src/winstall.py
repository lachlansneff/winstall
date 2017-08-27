import tempfile, requests, subprocess, sys, time
from threading import Timer

class Application:
    def __init__(self, name):
        self.name = name
    def download(self, url):
        self.downloadbar = Progress(msg='Downloading \''+self.name+'\'', success='\''+self.name+'\' downloaded')
        self.downloadbar.start()
        r = requests.get(url, stream=True)
        with tempfile.TemporaryFile() as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            self.downloadbar.stop()
            self.tempfile = f
    def install(self):
        self.installbar = Progress(msg='Installing \''+self.name+'\'', success='\''+self.name+'\' installed')
        self.installbar.start()
        self.process = subprocess.Popen([self.tempfile.name], creationflag=subprocess.CREATE_NO_WINDOW)
        self.installbar.stop()


class Progress:
    def __init__(self, type='indeterminate', msg='', success='', dotnum=3):
        self.type = type
        self.timer = None
        self.msg = msg
        self.success = success
        self.dotnum = dotnum
    def start(self):
        def recurse(i=0):
            sys.stdout.write('\r' + self.msg + ('.' * i) + ' '*(self.dotnum-i))
            sys.stdout.flush()
            self.timer = Timer(0.2, recurse, [(0 if i == self.dotnum else i+1)])
            self.timer.start()
        recurse()
    def stop(self):
        self.timer.cancel();
        print(success)

urls = {
    'hyper': 'https://releases.hyper.is/download/win',
    'git': 'https://central.github.com/deployments/desktop/desktop/latest/win32',
    'atom': 'https://atom.io/download/windows_x64'
}

apps = []

for name, url in urls.items():
    app = Application(name)
    app.download()
    apps.append(app)
for app in apps:
    app.install()
