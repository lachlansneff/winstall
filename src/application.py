import progress, subprocess, requests, tempfile

class App:
    def __init__(self, name, url, cmd_args=''):
        self.name = name
        self.url = url
        self.cmd_args = cmd_args
    def download(self):
        self.downloadbar = progress.Progress(msg='Downloading \''+self.name+'\'', success='\''+self.name+'\' downloaded')
        self.downloadbar.start()
        r = requests.get(self.url, stream=True)
        with tempfile.TemporaryFile() as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            self.downloadbar.stop()
            self.tempfile = f
    def install(self):
        self.installbar = progress.Progress(msg='Installing \''+self.name+'\'', success='\''+self.name+'\' installed')
        self.installbar.start()
        self.process = subprocess.Popen([self.tempfile.name] + cmd_args, creationflag=subprocess.CREATE_NO_WINDOW)
        self.installbar.stop()
