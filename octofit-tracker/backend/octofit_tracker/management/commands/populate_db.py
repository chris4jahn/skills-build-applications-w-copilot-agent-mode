from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write('Creating users...')
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        self.stdout.write('Creating workouts...')
        workout1 = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        workout2 = Workout.objects.create(name='Flight', description='Flying workout')
        workout1.suggested_for.set([spiderman, ironman])
        workout2.suggested_for.set([superman, batman])

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=spiderman, type='Cardio', duration=30, date='2025-11-13')
        Activity.objects.create(user=ironman, type='Strength', duration=45, date='2025-11-12')
        Activity.objects.create(user=batman, type='Stealth', duration=40, date='2025-11-11')
        Activity.objects.create(user=superman, type='Flight', duration=60, date='2025-11-10')

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write('Ensuring unique index on user email...')
        with connection.cursor() as cursor:
            cursor.execute('''db.users.createIndex({ "email": 1 }, { unique: true })''')

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
