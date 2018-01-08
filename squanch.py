from mp3fromrss import FindAndDownloadMissing
from mp3fromrss import DownloadedEpisodesManager
from mp3fromrss import WithDateOnBeginingDownloader
from mp3fromrss import Downloader

class Squanch(FindAndDownloadMissing):
    def __init__(self, logger, path):
        FindAndDownloadMissing.__init__(
            self,
            logger,
            DownloadedEpisodesManager(path),
            WithDateOnBeginingDownloader(
                logger,
                'http://squanch.libsyn.com/rss',
                Downloader()
            )
        )

    def _getName(self):
        return "Squanch"
