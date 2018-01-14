from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import FileNameWithDateOnBegining

class Niezatapialni(FindAndDownloadMissing):
    MainRSSLink = 'http://niezatapialni.com/?feed=rss2'
    FileNameManager = FileNameWithDateOnBegining()

    def getRSSLink(self):
        return self.MainRSSLink

    def getName(self):
        return "Niezatapialni"
