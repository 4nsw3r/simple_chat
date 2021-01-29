from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bl = models.ManyToManyField(User, blank=True, symmetrical=False, related_name='blacklist')

    def __str__(self):
        return self.user.username


# User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='sender_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='receiver_messages')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} to {}'.format(self.sender.username, self.receiver.username)
