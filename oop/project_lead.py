from leader import Leader


class ProjectLead(Leader):

    def __init__(self, name):
        self.name = name
        self.level = 'Project'
        self.role = 'manage'
        self.state = 'result of <gs>'
        self.schedule_url = 'Plan GSheet URL'

# with ProjectLead('Social Innovators Economy') as pl:
#     pl.lead()
