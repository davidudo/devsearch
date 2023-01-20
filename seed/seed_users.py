'''
  Copy this code and run it using
  >>>python manage.py shell
'''

from django_seed import Seed

seeder = Seed.seeder()

from users.models import Profile, Skill, Message
seeder.add_entity(Profile, 20)
seeder.add_entity(Skill, 100, {
    'name': lambda x: seeder.faker.word(),
})
seeder.add_entity(Message, 100)

inserted_pks = seeder.execute()
