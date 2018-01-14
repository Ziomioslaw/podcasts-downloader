class Episode():
    def __init__(self, publishDate, link):
        self.link = link
        self.publishDate = publishDate

    def getLink(self):
        return self.link

    def getPublishDate(self):
        return self.publishDate
