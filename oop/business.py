from business_lead import BusinessLead
from project_lead import ProjectLead


class Business(BusinessLead, ProjectLead):

    def __init__(self, name):
        BusinessLead.__init__(self, name)
        ProjectLead.__init__(self, name)
        self.name = name

    def __enter__(self):
        print('- start - Business: {}'.format(self.name))
        return self

    def __exit__(self, type, value, traceback):
        print('- close - Business: {}'.format(self.name))
        return self

    def launch(self):
        print('launch Business: {}'.format(self.name))


with Business('Coin Biz Skills') as biz, BusinessLead(biz) as owner, ProjectLead(biz) as pm:
    biz.launch()
    owner.lead()
    pm.lead()

print(biz.__dict__)
# print(owner)
# print(pm)
