class Skill:
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


# print.(Skill)

skill1 = Skill()
skill1.run()

# Skill.top_speed = 200
skill1.used_at.append('Marry Via Programming')
skill1.add_warning('New warning')
# skill1.__warnings.append([])
print(skill1)

skill2 = Skill(200)
skill2.run()
skill2.used_at.append('World Elections 2020')
print(skill2.used_at)
print(skill2.get_warnings())


skill3 = Skill(250)
skill3.run()
skill3.used_at.append('World Wide Skills Genom')
print(skill3.used_at)
print(skill3.get_warnings())
