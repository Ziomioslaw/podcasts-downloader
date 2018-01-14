class FileNameInLink():
    def getNameForEpisode(self, episode):
        return episode.getLink().rpartition('/')[-1]

