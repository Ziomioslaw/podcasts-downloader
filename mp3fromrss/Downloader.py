import urllib.request

class Downloader():
    def run(self, fromLink, toPath):
        urllib.request.urlretrieve(fromLink, toPath)
