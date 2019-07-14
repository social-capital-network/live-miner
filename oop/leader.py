class Leader():

    def __init__(self, name):
        self.name = name
        self.level = ''
        self.role = ''

    def __enter__(self):
        print(' - start - {}: {}'.format(self.level, self.name))
        return self

    def __exit__(self, type, value, traceback):
        print(' - close - {}: {}'.format(self.level, self.name))
        return self

    def __repr__(self):
        return '{} {}: {}'.format(self.role, self.level, self.name)

    def lead(self):
        print('{} {}: {}'.format(self.role, self.level, self.name))
