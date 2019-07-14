class ProjectLead():
    role = 'Project'
    ops = 'manage'

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('- start - {}: {}'.format(self.role, self.name))
        return self

    def __exit__(self, type, value, traceback):
        print('- close - {}: {}'.format(self.role, self.name))
        return self

    def lead(self):
        print('{} {}: {}'.format(self.ops, self.role, self.name))


# with ProjectLead('Social Innovators Economy') as pl:
#     pl.lead()
