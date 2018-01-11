class FindAndDownloadMissing():
    def __init__(self, logger, episodesManager, downloader, feedReader):
        self.logger = logger
        self.episodesManager = episodesManager
        self.downloader = downloader
        self.feedReader = feedReader

    def run(self):
        name = self._getName()

        self.logger.message('%s downloader start working' % name)

        lastEpisode = self.episodesManager.getLastDownloadedEpisodeName()
        if lastEpisode == None:
            self.logger.message('No downloaded episodes in given directory')
            self.downloadLastEpisode(self.episodesManager)
        else:
            self.logger.message('Last downloaded episode: "%s"' % lastEpisode)
            self.downloadAllEpisodeFrom(lastEpisode)

        self.logger.message('%s downloader finished' % name)

    def downloadLastEpisode(self):
        episode = next(self.feedReader.getNextEpisode())

        self.__downloadListedEpisodes([episode])

    def downloadAllEpisodeFrom(self, lastDownloadedEpisode):
        episodes = self.__getAllNewEpisodesList(lastDownloadedEpisode)

        if len(episodes) == 0:
            self.logger.message('No new episodes')
            return

        self.__downloadListedEpisodes(episodes)

    def __getAllNewEpisodesList(self, lastDownloadedEpisode):
        results = []
        for episode in self.feedReader.getNextEpisode():
            if lastDownloadedEpisode in episode.getLink():
                return results

            results.append(episode)

        return results

    def __downloadListedEpisodes(self, episodes):
        for episode in episodes:
            fileName = self._createForLink(episode)
            saveFilePath = episodesManager.getFullPathForFile(fileName)
            link = episode.getLink()

            self.logger.message('Download file from link "%s" to "%s"' % (link, saveFilePath))
            self.downloader.run(link, saveFilePath)

    def _getName(self):
        return "Unnamed"
