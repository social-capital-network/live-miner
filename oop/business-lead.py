class BusinessLead():
    role = 'lead'

    def __init__(self, project='Coin Your Skills'):
        self.project = project

    def __enter__(self):
        print('- starting - Project: {}'.format(self.project))
        return self

    def __exit__(self, type, value, traceback):
        print('- closing - Project: {}'.format(self.project))
        return self

    def lead(self):
        print('{}ing Project: {}'.format(self.role, self.project))


with BusinessLead('Social Innovators Economy') as bl:
    bl.lead()
