from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import FileNameInLink

class SGTTU(FindAndDownloadMissing):
    MainRSSLink = 'http://www.theskepticsguide.org/feed/rss.aspx'
    FileNameManager = FileNameInLink()

    def getName(self):
        return "SGTTU"
