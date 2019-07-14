class BusinessLead():
    level = 'Program'
    role = 'lead'

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(' - start - {}: {}'.format(self.level, self.name))
        return self

    def __exit__(self, type, value, traceback):
        print(' - close - {}: {}'.format(self.level, self.name))
        return self

    def lead(self):
        print('{} {}: {}'.format(self.role, self.level, self.name))


# with BusinessLead('Social Innovators Economy') as bl:
#     bl.lead()
