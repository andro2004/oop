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
class VotingSystem:
    def __init__(self):
        self.candidates = {}

    def add_candidate(self, candidate_name):
        if candidate_name not in self.candidates:
            self.candidates[candidate_name] = candidate(candidate_name)
            print(f'Candidate "{candidate_name}" added.')
        else:
            print(f'Candidate "{candidate_name}" is already added before.')

    def vote(self, candidate_name):
        if candidate_name in self.candidates:
            self.candidates[candidate_name].add_vote()
            print(f'Vote add for "{candidate_name}".')
        else:
            print(f'Candidate "{candidate_name}" not.')

    def get_results(self):
        max =0
        for cand in self.candidates.values():
            if cand.get_votes()>max:
                max=cand.get_votes()
        for cand in self.candidates.values():
            if cand.get_votes()==max:
                winner=cand.get_name()
        print( f'The winner is "{winner}" with {max} votes.')