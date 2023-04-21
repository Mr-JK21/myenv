from django.db import models
# import auth user modle 
from django.contrib.auth.models import User

class registery(models.Model):
    ROLE_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer')
    )
    # foreign key user_id 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    QUESTION_CHOICES = (
        ('nm', 'What is your favourite name ?'),
        ('no', 'What is your favourite number ?'),
        ('th', 'What is your favourtie thing ?')
    )
    question = models.CharField(max_length=100, choices=QUESTION_CHOICES)
    answer = models.CharField(max_length=100)
    role = models.CharField(max_length=11, choices=ROLE_CHOICES)
    # terms = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

