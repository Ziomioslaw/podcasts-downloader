import urllib

class Downloader():
    def run(fromLink, toPath):
        urllib.urlretrieve(link, saveFilePath)

class Mp3FromRSSDownloader():
    def __init__(self, logger, downloader):
        self.logger = logger
        self.downloader = downloader

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
            fileName = self._createForLink(episode)
            saveFilePath = episodesManager.getFullPathForFile(fileName)
            link = episode.getLink()

            self.logger.message('Download file from link "%s" to "%s"' % (link, saveFilePath))
            self.downloader.run(link, saveFilePath)

    def _createForLink(self, link):
        raise "Not implemented"

