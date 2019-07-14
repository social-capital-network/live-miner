class ProjectLead():

    def __init__(self, project='Coin Your Skills'):
        self.project = project

    def __enter__(self):
        print('- starting - Project: {}'.format(self.project))
        return self

    def __exit__(self, type, value, traceback):
        print('- closing - Project: {}'.format(self.project))
        return self

    def lead(self):
        print('leading Project: {}'.format(self.project))


with ProjectLead('Social Innovators Economy') as pl:
    pl.lead()
