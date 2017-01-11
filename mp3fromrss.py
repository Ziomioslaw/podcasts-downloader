#!/usr/bin/python

import urllib, os

class Mp3FromRSSDownloader():
    def __init__(self, logger, episodesDirectory):
        self.logger = logger
        self.episodesDirectory = episodesDirectory

    def run(self):
        self.logger.message('%s downloader start working' % self._getName())

        episodes = self._getDownloadedEpisodesList()
        episode = self._getLastDownloadedEpisodeName(episodes)

        if episode == None:
            self.logger.message('No downloaded episodes in given directory')

        else:
            self.logger.message('Last downloaded episode: "%s"' % episode)
            self._downloadAllEpisodeFrom(episode)

    def _getDownloadedEpisodesList(self):
        files = os.listdir(self.episodesDirectory)
        results = [f[:len(f) - 4].lower() for f in files if os.path.isfile(os.path.join(self.episodesDirectory, f)) and f.endswith('.mp3')]
        return results

    def _getLastDownloadedEpisodeName(self, episodes):
        episodes.sort()

        if len(episodes) > 0:
            return episodes[-1].lower()
        else:
            return None

    def _downloadAllEpisodeFrom(self, lastDownloadedEpisode):
        links = self._findAllNewEpisodes(lastDownloadedEpisode)

        if (len(links) == 0):
            self.logger.message('No new episodes')
            return

        for link in links:
            self.logger.message('Download file from link: %s' % link)
            saveFilePath = self._getMP3SaveFilePath(link)
            urllib.urlretrieve(link, saveFilePath)

    def _getMP3SaveFilePath(self, link):
        raise "Not implemented _getMP3SaveFilePath method"

    def _getName(self):
        return "unnamed"

import datetime

class FakeDaemonPrintingOnOut():
    def message(self, msg):
        date = datetime.datetime.now()
        print '[%s] %s' % (date.strftime('%Y-%m-%d %H:%M:%S'), msg)
