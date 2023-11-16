class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        if self.muted:
            self.muted = False
        else:
            self.muted = True

