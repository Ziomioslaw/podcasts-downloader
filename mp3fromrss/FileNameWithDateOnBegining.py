class FileNameWithDateOnBegining():
    def getNameForEpisode(self, episode):
        onlyFileNameWithParamaters = episode.getLink().rpartition('/')[-1]
        onlyFileName = onlyFileNameWithParamaters.partition('?')[0].lower()

        return '[%s] %s' % (episode.getPublishDate().strftime('%Y%m%d'), onlyFileName)
