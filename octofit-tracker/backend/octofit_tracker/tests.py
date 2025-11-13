from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        self.activity = Activity.objects.create(user=self.user, type='Cardio', duration=30, date='2025-11-13')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Marvel')

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Web Swing')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Cardio')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)
