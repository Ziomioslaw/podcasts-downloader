from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import WithDateOnBeginingDownloader
from mp3fromrss import DownloadedEpisodesManager
from mp3fromrss import Downloader

class Niezatapialni(FindAndDownloadMissing):
    def __init__(self, logger, path):
        FindAndDownloadMissing.__init__(
            self,
            logger,
            DownloadedEpisodesManager(path),
            WithDateOnBeginingDownloader(
                logger,
                'http://niezatapialni.com/?feed=rss2',
                Downloader()
            )
        )

    def _getName(self):
        return "Niezatapialni"
