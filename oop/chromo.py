class Chromo:
    top_record = 100
    changes = []
    used_at = ['Visa']
    last_used = ''
    species_url = 'Github'
    chromozome_api = 'programming'

    def __init__(self, starting_top_speed=100):
        self.protocol = 'W3AI'
        self.top_speed = starting_top_speed
        self.__warnings = []
        self.source = 'github'
        self.exec = 'npm'

    def __repr__(self):
        print('Printing...')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed, len(self.__warnings))

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def get_warnings(self):
        return self.__warnings

    def run(self):
        print('I am operating not faster than {}'.format(self.top_speed))
