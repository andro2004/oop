class candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def add_vote(self):
        self.votes += 1

    def get_votes(self):
        return self.votes
    def get_name(self):
        return self.name