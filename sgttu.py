#!/usr/bin/python

import os
import feedparser
from mp3fromrss import Mp3FromRSSDownloader

class SGTTUDownloader(Mp3FromRSSDownloader):
    MainRSSLink = 'http://www.theskepticsguide.org/feed/rss.aspx'
    DownloadServerDirectory = 'http://media.libsyn.com/media/skepticsguide/'

    def _findAllNewEpisodes(self, lastDownloadedEpisode):
        feed = feedparser.parse(self.MainRSSLink)
        items = feed['items']
        results = []

        for item in items:
            link = item['links'][0]['href']

            if lastDownloadedEpisode in link:
                return results

            results.append(link)

        return results

    def _getMP3SaveFilePath(self, link):
        return os.path.join(self.episodesDirectory, link[len(self.DownloadServerDirectory):])

    def _getName(self):
        return "SGTTU"
