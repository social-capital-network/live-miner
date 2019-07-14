class Leader:

    def __init__(self, project):
        self.project = project

    def __enter__(self):
        print('- starting - Project: {}'.format(self.project))
        return self

    def __exit__(self, type, value, traceback):
        print('- closing - Project: {}'.format(self.project))
        return self
