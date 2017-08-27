import subprocess, progress

class Feature:
    def __init__(self, featurename):
        self.featurename = featurename
    def install(self):
        self.installbar = progress.Progress(msg='Enabling \''+self.featurename+'\'', success='\''+self.featurename+'\' enabled')
        self.installbar.start()
        self.process = subprocess.Popen(['runas', '/user:Administrator', 'dism /online /enable-feature /featurename:'+self.featurename])
        self.process.wait()
        self.installbar.stop()
