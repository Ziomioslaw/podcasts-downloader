import asyncio

from mp3fromrss import Downloader
from mp3fromrss import DownloadedEpisodesManager
from mp3fromrss import FeedReader
from mp3fromrss import LiveFeedSource

from podcasts import *

class Runner():
    def __init__(self, logger):
        self.logger = logger
        self.downloader = Downloader()
        self.tasks = []

    def add(self, podcastName, path):
        podcast = globals()[podcastName]
        self.tasks.append(podcast(
            self.logger,
            self.getDownloadedEpisodesManager(path),
            self.downloader,
            self.getFeedReader(podcast.MainRSSLink),
            podcast.FileNameManager
        ).run())

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(self.tasks))
        loop.close()

    def getDownloadedEpisodesManager(self, path):
        return DownloadedEpisodesManager(path)

    def getFeedReader(self, rssLink):
        return FeedReader(LiveFeedSource(rssLink))
