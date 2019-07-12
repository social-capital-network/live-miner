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
        self.warnings = []
        self.source = 'github'
        self.exec = 'npm'

    def __repr__(self):
        print('Printing...')
        return 'Top Speed: {}, Warnings: {}'.format(self.top_speed, len(self.warnings))

    def run(self):
        print('I am operating not faster than {}'.format(self.top_speed))


# print.(Skill)

skill1 = Skill()
skill1.run()

# Skill.top_speed = 200
skill1.used_at.append('Marry Via Programming')
skill1.warnings.append('New warning')
print(skill1)

skill2 = Skill(200)
skill2.run()
skill2.used_at.append('World Elections 2020')
print(skill2.used_at)
print(skill2.warnings)


skill3 = Skill(250)
skill3.run()
skill3.used_at.append('World Wide Skills Genom')
print(skill3.used_at)
print(skill3.warnings)
