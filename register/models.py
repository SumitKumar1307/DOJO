from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    key = models.CharField(max_length=500)

    def __str__(self):
        return f'username: {self.username};\nemail: {self.email};\npassword={self.password};\nkey: {self.key}'

class Key(models.Model):
    key = models.CharField(max_length=200)
    # id = IntegerField(max_length=10000)
