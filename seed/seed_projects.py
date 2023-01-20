'''
  Copy this code and run it using
  >>>python manage.py shell
'''

from django_seed import Seed

seeder = Seed.seeder()

from projects.models import Project, Review, Tag
seeder.add_entity(Project, 50)
seeder.add_entity(Review, 200)
seeder.add_entity(Tag, 150)

'''{
    'name': lambda x: seeder.faker.word(),
}'''

inserted_pks = seeder.execute()
