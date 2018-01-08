
class FindAndDownloadMissing():
    def __init__(self, logger, episodesManager, downloaderManager):
        self.logger = logger
        self.episodesManager = episodesManager
        self.downloaderManager = downloaderManager

    def run(self):
        name = self._getName()

        self.logger.message('%s downloader start working' % name)

        lastEpisode = self.episodesManager.getLastDownloadedEpisodeName()
        if lastEpisode == None:
            self.logger.message('No downloaded episodes in given directory')
            self.downloaderManager.downloadLastEpisode(self.episodesManager)
        else:
            self.logger.message('Last downloaded episode: "%s"' % lastEpisode)
            self.downloaderManager.downloadAllEpisodeFrom(lastEpisode, self.episodesManager)

        self.logger.message('%s downloader finished' % name)

    def _getName(self):
        return "Unnamed"
