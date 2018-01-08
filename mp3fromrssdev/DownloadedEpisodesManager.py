import os

class DownloadedEpisodesManager():
    def __init__(self, episodesList):
        self.episodesList = episodesList

    def getPath(self):
        return '/var/tmp/'

    def getLastDownloadedEpisodeName(self):
        episodes = self.getDownloadedEpisodesList()
        episodes.sort()

        if len(episodes) > 0:
            return episodes[-1].lower()
        else:
            return None

    def getDownloadedEpisodesList(self):
        return self.episodesList

    def getFullPathForFile(self, fileName):
        self.episodesList.append(fileName)

        return os.path.join(self.getPath(), fileName)
