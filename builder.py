from mp3fromrss import Downloader
from mp3fromrss import DownloadedEpisodesManager
from mp3fromrss import FeedReader
from mp3fromrss import LiveFeedSource

from niezatapialni import Niezatapialni
from sgttu import SGTTU
from squanch import Squanch

class Builder():
    def __init__(self, logger):
        self.logger = logger
        self.downloader = Downloader()

    def build(self, podcastName, path):
        podcast = globals()[podcastName]

        return podcast(
            self.logger,
            self.getDownloadedEpisodesManager(path),
            self.downloader,
            self.getFeedReader(podcast.MainRSSLink),
            podcast.FileNameManager
        )

    def getDownloadedEpisodesManager(self, path):
        return DownloadedEpisodesManager(path)

    def getFeedReader(self, rssLink):
        return FeedReader(LiveFeedSource(rssLink))
