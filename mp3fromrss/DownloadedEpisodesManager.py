import os

class DownloadedEpisodesManager():
    def __init__(self, episodesDirectory):
        self.episodesDirectory = episodesDirectory

    def getPath(self):
        return self.episodesDirectory

    async def getLastDownloadedEpisodeName(self):
        episodes = await self.getDownloadedEpisodesList()
        episodes.sort()

        if episodes:
            return episodes[-1].lower()

        return None

    async def getDownloadedEpisodesList(self):
        files = os.listdir(self.episodesDirectory)
        results = [f[:len(f) - 4].lower() for f in files if os.path.isfile(os.path.join(self.episodesDirectory, f)) and (f.endswith('.mp3') or f.endswith('.m4v'))]

        return results

    def getFullPathForFile(self, fileName):
        return os.path.join(self.episodesDirectory, fileName)
