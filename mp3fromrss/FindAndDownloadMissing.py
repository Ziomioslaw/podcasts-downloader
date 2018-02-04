class FindAndDownloadMissing():
    def __init__(self, logger, episodesManager, downloader, feedReader, fileNameManager):
        self.logger = logger
        self.episodesManager = episodesManager
        self.downloader = downloader
        self.feedReader = feedReader
        self.fileNameManager = fileNameManager

    def run(self):
        name = self.getName()

        self.logger.message('{} downloader start working', name)

        lastEpisode = self.episodesManager.getLastDownloadedEpisodeName()
        if lastEpisode == None:
            self.logger.message('No downloaded episodes in given directory')
            self.downloadLastEpisode(self.episodesManager)
        else:
            self.logger.message('Last downloaded episode: "{}"', lastEpisode)
            self.downloadAllEpisodeFrom(lastEpisode)

        self.logger.message('{} downloader finished', name)

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
            episodeName = self.fileNameManager.getNameForEpisode(episode)

            if lastDownloadedEpisode in episodeName:
                return results

            results.append(episode)

        return results

    def __downloadListedEpisodes(self, episodes):
        for episode in episodes:
            fileName = self.fileNameManager.getNameForEpisode(episode)
            saveFilePath = self.episodesManager.getFullPathForFile(fileName)
            link = episode.getLink()

            self.logger.message('Download file from link "{}" to "{}"', [link, saveFilePath])
            self.downloader.run(link, saveFilePath)

    def getName(self):
        return "Unnamed"