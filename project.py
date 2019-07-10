from time import time

from block import Block

# Class Project is similar to the Block class considering transactions equivalent to contributions (including non monetary) and proof equivalent to Test Proofs
# ToDo: Add Project initialization, Owner, PM, Repo, Charter, Governance etc


class Project(Block):
    phase = 'idea' | 'project' | 'service' | 'archive'
    kind = 'agile' | 'waterfall'
    state = 'active'
    status = 'genesis commit'
    changes = 1         # each change is a block
    branches = 1        # git branches
    contexts = 1        # at least 1
    solutions = 0
    implementations = 0
    creators = 1
    contributors = 1
    copies = 1
    voters = 1
    votes = 1
    creators = 1
    founders = 1
    owners = 1
    shareholders = 1
    budget = 5

    def __init__(self, index, title, subtitle, tags, description):
        self.index = index
        self.title = title
        self.subtitle = subtitle
        self.tags = tags
        self.description = description


class Sprint(Block):
    def __init__(self, index, duration):
        self.index = index
        self.duration = duration
