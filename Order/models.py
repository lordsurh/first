from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime
from django.db import models
from django.contrib.auth.models import User
import hashlib


class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    favourite_snack = models.CharField(_('favourite snack'),
                                       max_length=5)

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    poll_section = (
        ('Sport', 'Sport'),
        ('Animation', 'Animation'),
        ('Health', 'Health'),
        ('Business', 'Business'),
        ('Lifestyle','Lifestyle'),
        )
    poll__section = models.CharField(max_length=60, choices=poll_section)



    def was__published__recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was__published__recently.boolean = True

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.text

class Voter(models.Model):
    user = models.ForeignKey(User)
    poll = models.ForeignKey(Poll)









