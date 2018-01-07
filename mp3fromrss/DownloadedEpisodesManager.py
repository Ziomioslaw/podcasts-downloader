import urllib, os

class DownloadedEpisodesManager():
    def __init__(self, episodesDirectory):
        self.episodesDirectory = episodesDirectory

    def getPath(self):
        return self.episodesDirectory

    def getLastDownloadedEpisodeName(self):
        episodes = self.getDownloadedEpisodesList()
        episodes.sort()

        if len(episodes) > 0:
            return episodes[-1].lower()
        else:
            return None

    def getDownloadedEpisodesList(self):
        files = os.listdir(self.episodesDirectory)
        results = [f[:len(f) - 4].lower() for f in files if os.path.isfile(os.path.join(self.episodesDirectory, f)) and f.endswith('.mp3')]

        return results

    def getFullPathForFile(self, fileName):
        return os.path.join(self.episodesDirectory, fileName)
