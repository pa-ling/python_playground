class CrawledArticle():
    def __init__(self, title, emoji, content, image):
        self.title = title
        self.emoji = emoji
        self.content = content
        self.image = image

    def __repr__(self):
        return self.emoji + ":" + self.title
