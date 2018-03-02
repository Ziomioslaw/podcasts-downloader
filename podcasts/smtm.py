from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import FileNameWithDateOnBegining

class SMTM(FindAndDownloadMissing):
    MainRSSLink = 'https://showmethemeaning.libsyn.com/rss'
    FileNameManager = FileNameWithDateOnBegining()

    def getRSSLink(self):
        return self.MainRSSLink

    def getName(self):
        return "Show Me The Meaning!"
