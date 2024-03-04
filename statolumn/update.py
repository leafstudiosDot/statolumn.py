class Update:
    media = None
    def __init__(self, content):
        self.content = content
        pass

    def attachMedia(self, media):
        self.media = media
        pass

    def update(self, client):
        pass