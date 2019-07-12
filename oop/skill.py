class Skill:
    top_speed = 100
    changes = []
    used_at = ['Visa']
    warnings = []

    def __init__():

    def run(self):
        print('I am operating not faster than {}'.format(self.top_speed))


skill1 = Skill()
skill1.run()

# Skill.top_speed = 200
skill1.used_at.append('Marry Via Programming')

skill2 = Skill()
skill2.run()
skill2.used_at.append('World Elections 2020')
print(skill2.used_at)


skill3 = Skill()
skill3.run()
skill3.used_at.append('World Wide Skills Genom')
print(skill3.used_at)
