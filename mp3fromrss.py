#!/usr/bin/python

import urllib, os

class FindAndDownloadMissing():
    def __init__(self, logger, episodesManager, downloader):
        self.logger = logger
        self.episodesManager = episodesManager
        self.downloader = downloader

    def run(self):
        name = self._getName()

        self.logger.message('%s downloader start working' % name)

        lastEpisode = self.episodesManager.getLastDownloadedEpisodeName()
        if lastEpisode == None:
            self.logger.message('No downloaded episodes in given directory')
            self.downloader.downloadLastEpisode(self.episodesManager)
        else:
            self.logger.message('Last downloaded episode: "%s"' % lastEpisode)
            self.downloader.downloadAllEpisodeFrom(lastEpisode, self.episodesManager)

        self.logger.message('%s downloader finished' % name)

    def _getName(self):
        return "Unnamed"

class Mp3FromRSSDownloader():
    def __init__(self, logger):
        self.logger = logger

    def downloadLastEpisode(self, episodesManager):
        episode = next(self._getNextEpisode())

        self._downloadListedEpisodes([episode], episodesManager)

    def downloadAllEpisodeFrom(self, lastDownloadedEpisode, episodesManager):
        episodes = self._findAllNewEpisodes(lastDownloadedEpisode)

        if len(episodes) == 0:
            self.logger.message('No new episodes')
            return

        self._downloadListedEpisodes(episodes, episodesManager)

    def _downloadListedEpisodes(self, episodes, episodesManager):
        for episode in episodes:
            fileName = self._createForLink(episode.getLink())
            saveFilePath = episodesManager.getFullPathForFile(fileName)
            link = episode.getLink()

            self.logger.message('Download file from link "%s" to "%s"' % (link, saveFilePath))
            urllib.urlretrieve(link, saveFilePath)

    def _createForLink(self, link):
        raise "Not implemented"

class Episode():
    def __init__(self, publishDate, link):
        self.link = link
        self.publishDate = publishDate

    def getLink(self):
        return self.link

    def getPublishDate(self):
        return self.publishDate

class DownloadedEpisodesManager():
    def __init__(self, episodesDirectory):
        self.episodesDirectory = episodesDirectory

    def getPath(self):
        return self.episodesDirectory

    def getLastDownloadedEpisodeName(self):
        episodes = self.getDownloadedEpisodesList()
        episodes.sort()

        if len(episodes) > 0:
            return episodes[-1].lower()
        else:
            return None

    def getDownloadedEpisodesList(self):
        files = os.listdir(self.episodesDirectory)
        results = [f[:len(f) - 4].lower() for f in files if os.path.isfile(os.path.join(self.episodesDirectory, f)) and f.endswith('.mp3')]

        return results

    def getFullPathForFile(self, fileName):
        return os.path.join(self.episodesDirectory, fileName)

import datetime

class FakeDaemonPrintingOnOut():
    def message(self, msg):
        date = datetime.datetime.now()
        print '[%s] %s' % (date.strftime('%Y-%m-%d %H:%M:%S'), msg)
