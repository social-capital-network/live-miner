class BusinessLead():
    role = 'lead'

    def __init__(self, project):
        self.project = project

    def __enter__(self):
        print(' - start - Project: {}'.format(self.project))
        return self

    def __exit__(self, type, value, traceback):
        print(' - close - Project: {}'.format(self.project))
        return self

    def lead(self):
        print(' {} Project: {}'.format(self.role, self.project))


# with BusinessLead('Social Innovators Economy') as bl:
#     bl.lead()
