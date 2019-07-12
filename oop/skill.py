class Skill:
    top_speed = 100
    changes = []
    projects = ['Visa']
    warnings = []

    def run(self):
        print('I am operating not faster than {}'.format(self.top_speed))


skill1 = Skill()
skill1.run()

# Skill.top_speed = 200
skill1.projects.append('Mary Via Programming')

skill2 = Skill()
skill2.run()
skill2.projects.append('World Elections 2020')
print(skill2.projects)


skill3 = Skill()
skill3.run()
skill3.projects.append('World Wide Web Skills Genom')
print(skill3.projects)
