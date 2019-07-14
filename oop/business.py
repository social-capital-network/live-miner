from business_lead import BusinessLead
# from project_lead import ProjectLead


class Business(BusinessLead):

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def __enter__(self):
        print('- start - Business: {}'.format(self.name))
        return self

    def __exit__(self, type, value, traceback):
        print('- close - Business: {}'.format(self.name))
        return self

    def launch(self):
        print('launch Business: {}'.format(self.name))


with Business('Coin Biz Skills') as biz, BusinessLead(biz) as owner:
    biz.launch()
    owner.lead()
