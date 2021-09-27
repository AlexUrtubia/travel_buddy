from django.db import models
import re
import bcrypt
from datetime import date

class UserManager(models.Manager):
    def basic_validator(self, postData):
        # today = date.today()
        # age = postData['birthday']
        errors = {}
        if len(User.objects.filter(user_name=postData['user_name'])) > 0:
            errors['exists'] = "User name already registered"
        else:
            if len(postData['name']) == 0:
                errors['no_name'] = "You must provide a name"
            if len(postData['name']) < 3 and len(postData['name'])  != 0:
                errors['c_name'] = "Name must have at least 3 characters"
            if len(postData['user_name']) == 0:
                errors['no_user_name'] = "You must provide a user name"
            if len(postData['user_name']) < 3 and len(postData['user_name']) != 0:
                errors['user_name'] = "User name must have at least 3 characters"
            # if len(postData['email']) == 0:
            #     errors['no_email'] = "You must provide a email"
            # EMAIL = re.compile(
            # r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            # if not EMAIL.match(postData['email']):
            #     errors['email'] = "Invalid email"
            if len(postData['password']) == 0:
                errors['no_password'] = "You must provide a password"
            if len(postData['password']) < 8 and len(postData['password']) != 0:
                errors['no_password'] = "Your password must have at least 8 characters"
            if postData['password'] != postData['password_c']:
                errors['password_c'] = "Passwords don't match"
            # if postData['birthday'] > str(today):
            #     errors['birthday'] = 'Birthday must be past!'
            # if age.year() - postData['birthday'].year() < 13:
            #     errors['under_age'] = 'You must be at least 13 years old!'
        return errors

    def encriptar(self, password):
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return password

    def login_validator(self, password, user):
        errors = {}
        if len(user) > 0:
            # pw_given = postData['password']
            pw_hash = user[0].password
            if bcrypt.checkpw(password.encode(), pw_hash.encode()) is False:
                errors['wrong_pass'] = "Wrong password"
        else:
            errors['invalid_user'] = "User does not exist"
        return errors

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    #email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()