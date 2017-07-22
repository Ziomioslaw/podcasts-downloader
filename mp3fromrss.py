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
            self.downloader.downloadLastEpisode()
        else:
            self.logger.message('Last downloaded episode: "%s"' % lastEpisode)
            self.downloader.downloadAllEpisodeFrom(lastEpisode)

        self.logger.message('%s downloader finished' % name)

    def _getName(self):
        return "Unnamed"

class Mp3FromRSSDownloader():
    def __init__(self, logger):
        self.logger = logger

    def downloadLastEpisode(self):
        link = next(self._getNextEpisode())

        self._downloadListedEpisodes([link])

    def downloadAllEpisodeFrom(self, lastDownloadedEpisode):
        links = self._findAllNewEpisodes(lastDownloadedEpisode)

        if len(links) == 0:
            self.logger.message('No new episodes')
            return

        self._downloadListedEpisodes(links)

    def _downloadListedEpisodes(self, links):
        for link in links:
            fileName = self._createForLink(link)
            saveFilePath = self.episodesManager.getFullPathForFile(fileName)

            self.logger.message('Download file from link "%s" to "%s"' % (link, saveFilePath))
            urllib.urlretrieve(link, saveFilePath)

    def _createForLink(self, link):
        raise "Not implemented"

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
