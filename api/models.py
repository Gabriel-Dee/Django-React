from django.db import models
import string
import random


def generate_random_code():
    length =6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.

# A model is the single, definitive source of information about your data. 
# It contains the essential fields and behaviors of the data you’re storing. 
# Generally, each model maps to a single database table.

# Django is telling us to have fat models and thin views,
# Meaning most of the logic in django should be placed in Models and not views

class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True) 
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)