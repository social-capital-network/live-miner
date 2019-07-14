class Business():

    def __init__(self, name='AI Economy'):
        self.name = name

    def __enter__(self):
        print('- start - Business: {}'.format(self.name))
        return self

    def __exit__(self, type, value, traceback):
        print('- close - Business: {}'.format(self.name))
        return self

    def launch(self):
        print('launch Business: {}'.format(self.name))


with Business('Coin Biz Skills') as biz:
    biz.launch()
