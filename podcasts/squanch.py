from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import FileNameWithDateOnBegining

class Squanch(FindAndDownloadMissing):
    MainRSSLink = 'http://squanch.libsyn.com/rss'
    FileNameManager = FileNameWithDateOnBegining()

    def getRSSLink(self):
        return self.MainRSSLink

    def getName(self):
        return "Squanch"
