from chromo import Chromo


class Skill(Chromo):

    def brag(self):
        print('Cool skill to clone!')

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
