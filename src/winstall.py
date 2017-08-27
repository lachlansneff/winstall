import tempfile, requests, subprocess

def download(url):
    r = requests.get(self.url, stream=True)
    with tempfile.TemporaryFile() as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
        return f

def install(tempfile):
    process = subprocess.Popen([tempfile.name], creationflag=CREATE_NO_WINDOW)
    return process

urls = {
    'hyper': 'https://releases.hyper.is/download/win',
    'git': 'https://central.github.com/deployments/desktop/desktop/latest/win32',
    'atom': 'https://atom.io/download/windows_x64'
}

for name, url in urls.items():
    print('Downloading '+name+'...')
    f = download(url)
    print('Installing...')
    install(f).wait()
    print(name+' installed')
