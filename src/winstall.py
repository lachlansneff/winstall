import tempfile, requests, subprocess

class Download:
    def __init__(self, url):
        self.url = url
        r = requests.get(self.url, stream=True)
        with tempfile.TemporaryFile() as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            self.tempfile = f
    def execute(self):
        self.process = subprocess.Popen([self.tempfile.name])
    def wait(self):
        self.process.wait()

class Winstall:
    def __init__(self, url, isInstaller=True):
        self.url = url
        self.isInstaller = isInstaller
    def install(self):
        if (isInstaller):
            dl = Download(self.url)
            dl.execute()
            dl.wait()
            return True
