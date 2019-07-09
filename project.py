from time import time


class Project:
    def __init__(self, index, parent_hash, contributions, test_proof, time=time()):
        self.index = index
        self.parent_hash = parent_hash
        self.timestamp = time
        self.contributions = contributions
        self.test_proof = test_proof
