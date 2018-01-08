import urllib

class Downloader():
    def run(self, fromLink, toPath):
        urllib.urlretrieve(fromLink, toPath)
