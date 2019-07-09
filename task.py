from collections import OrderedDict

# The Task class should extend/adapt transaction as:
# sender => resource / task executant (that needs to be engaged, informed, scheduled, and payed)
# recipient => project owner and/or project manager
# amount => cost for the planning, execution and test of the task - these to be managed by a Deal Class
# ToDo: add classes for Deal (Contract ~ like DApps) Plan and Test


class Task:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __repr__(self):
        return str(self.__dict__)

    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])
