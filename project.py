from time import time

# Class Project is similar to the Block class considering transactions equivalent to contributions (including non monetary) and proof equivalent to Test Proofs
# ToDo: Add Project initialization, Owner, PM, Repo, Charter, Governance etc


class Project:
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof

# Class Sprint is similar to the Block class considering transactions equivalent to contributions (including non monetary) and proof equivalent to Test Proofs
# ToDo: Add Sprint Duration, and Agile Project initialization, Product Owner, SM, Repo, Charter, Governance etc

    def __repr__(self):
        return 'Milestones Index: {}, Previous Hash: {}, QA Proof: {}, Contributions: {}'.format(self.index, self.previous_hash, self.proof, self.transactions)


class Sprint:
    def __init__(self, index, previous_hash, transactions, proof, time=time()):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time
        self.transactions = transactions
        self.proof = proof

    def __repr__(self):
        return 'Milestones Index: {}, Previous Hash: {}, QA Proof: {}, Contributions: {}'.format(self.index, self.previous_hash, self.proof, self.transactions)
