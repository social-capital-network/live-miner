from collections import OrderedDict

from utility.printable import Printable


class Transaction(Printable):
    """A transaction (TASK) which can be added 
    to a SPRINT block in the PROJECT blockchain.

    Attributes:
        :sender: The service/skill owner.
        :recipient: The project on which the task is executed.
        :signature: The signature of the transaction.
        :amount: The cost of the task (as per contract).
        :duration: The duration of the task.
        :result: The result of the task.
    """

    def __init__(self, sender, recipient, signature, amount, duration, result):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature
        self.duration = duration
        self.result = result

    def to_ordered_dict(self):
        """Converts this transaction into a (hashable) OrderedDict."""
        return OrderedDict([('sender', self.sender),
                            ('recipient', self.recipient),
                            ('amount', self.amount),
                            ('duration', self.duration),
                            ('result', self.result)])
