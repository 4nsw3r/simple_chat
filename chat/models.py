from django.contrib.auth.models import User, AbstractUser
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    bl = models.ManyToManyField(User, blank=True, related_name='blacklist')

    def __str__(self):
        return self.user.username

class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='sender_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='receiver_messages')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} to {}'.format(self.sender.username, self.receiver.username)
