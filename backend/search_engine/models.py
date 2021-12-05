from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    cluster = []

    def addCluster(self, clus):
        self.cluster.append(clus)

    def __str__(self):
        return f'{self.user.username} Profile'

class ToBeSearched(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clusterName = models.CharField(max_length=100)
    depth = models.CharField(max_length=100)
    strategy = models.CharField(max_length=100)

class Cluster(models.Model):
    clusterName = models.CharField(max_length=100)

    link = []

    def addLink(self, link):
        self.link.append(link)

class Link(models.Model):
    url = models.CharField(max_length=1000)
    content = models.TextField()
