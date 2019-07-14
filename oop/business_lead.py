from leader import Leader


class BusinessLead(Leader):

    def __init__(self, name):
        self.name = name
        self.level = 'Program'
        self.role = 'lead'
        self.budget = 1000
        self.backlog_url = 'Backlog GSheet URL'


# with BusinessLead('Social Innovators Economy') as bl:
#     bl.lead()
