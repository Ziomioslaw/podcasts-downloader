#!/usr/bin/python

import os
import feedparser
from mp3fromrss import Mp3FromRSSDownloader

class SGTTUDownloader(Mp3FromRSSDownloader):
    MainRSSLink = 'http://www.theskepticsguide.org/feed/rss.aspx'
    DownloadServerDirectory = 'http://media.libsyn.com/media/skepticsguide/'

    def _getNextEpisode(self, link):
        feed = feedparser.parse(link)
        items = feed['items']

        for item in items:
            link = item['links'][0]['href']
            yield link

    def _findAllNewEpisodes(self, lastDownloadedEpisode):
        results = []
        for link in self._getNextEpisode(self.MainRSSLink):
            if lastDownloadedEpisode in link:
                return results

            results.append(link)

        return results

    def _getMP3SaveFilePath(self, link):
        return os.path.join(self.episodesDirectory, link[len(self.DownloadServerDirectory):])

    def _getName(self):
        return "SGTTU"
