#!/usr/bin/python

import urllib, os

class Mp3FromRSSDownloader():
    def __init__(self, parentDaemon, episodesDirectory):
        self.parentDaemon = parentDaemon
        self.episodesDirectory = episodesDirectory
        self.name = 'unnamed'
    
    def run(self):
        self.parentDaemon.message(self.name + ' Downloader start working')

        episodes = self._getDownloadedEpisodesList()
        episode = self._getLastDownloadedEpisodeName(episodes)
        
        self.parentDaemon.message('Last downloaded episode: "' + episode + '"')
        self._downloadAllEpisodeFrom(episode)

    def _getDownloadedEpisodesList(self):
        files = os.listdir(self.episodesDirectory)
        results = [f[:len(f) - 4].lower() for f in files if os.path.isfile(self.episodesDirectory + '/' + f) and f.endswith('.mp3')]
        return results

    def _getLastDownloadedEpisodeName(self, episodes):
        episodes.sort()
        return episodes[-1].lower()

    def _downloadAllEpisodeFrom(self, lastDownloadedEpisode):
        links = self._findAllNewEpisodes(lastDownloadedEpisode)

        if (len(links) == 0):
            self.parentDaemon.message('No new episodes')
            return

        for link in links:
            self.parentDaemon.message('Download file from link: ' + link)
            saveFilePath = self._getMP3SaveFilePath(link)
            urllib.urlretrieve(link, saveFilePath)

    def _getMP3SaveFilePath(self, link):
        raise "Not implemented _getMP3SaveFilePath method"

import datetime
		
class FakeDaemonPrintingOnOut():
    def message(self, msg):
        date = datetime.datetime.now()
        print '[' + date.strftime('%Y-%m-%d %H:%M:%S') + '] ' + msg

