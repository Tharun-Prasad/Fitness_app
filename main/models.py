from django.db import models
from django.contrib.auth.models import User

# Create your models here

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
    
class Measurement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    bmi = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'
    
# main/models.py

class Workouts(models.Model):
    WORKOUT_TYPES = [
        ('gain', 'gain'),
        ('lose', 'lose'),
        # Add more workout types as needed
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    workout_type = models.CharField(max_length=50, choices=WORKOUT_TYPES,default='gain')
    image = models.ImageField(upload_to='workouts/')

    def __str__(self):
        return self.name
    
class WorkoutPlans(models.Model):
    TYPES = [
        (15, 15),
        (30, 30),
        # Add more plans as needed
    ]
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='workouts/')
    days = models.IntegerField(default=15,choices=TYPES)
    description = models.TextField(max_length=500)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'days'], name='unique_title_days')
        ]

class UserProgress(models.Model):
   
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
    unique_title_days = models.ForeignKey(WorkoutPlans, on_delete=models.CASCADE)
    no_days = models.IntegerField(default=0)