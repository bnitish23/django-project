from django.db import models

# Create your models here.
class Venue(models.Model):
    name=models.CharField('Venue name', max_length=60)
    address=models.TextField()
    zipcode=models.CharField('Zipcode',max_length=6)
    phone=models.CharField('contact',max_length=10)
    web=models.URLField('Website address')
    email_address=models.EmailField('Email address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    email=models.EmailField('User Email address')


    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name=models.CharField('Event Name',max_length=120)
    event_date=models.DateTimeField('Event Date')
    Venue=models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #venue=models.CharFeild(max_length=120)
    manager=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    attendees=models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
