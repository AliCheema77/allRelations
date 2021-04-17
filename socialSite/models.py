from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date_join = models.DateField()

    def __str__(self):
        return self.name


class Page(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    page_title = models.CharField(max_length=70)
    page_creations = models.DateField()

    def __str__(self):
        return self.page_title


class Post(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    post_title= models.TextField()
    post_pub_date=models.DateField()


    


class Song(models.Model):
    wah= models.ManyToManyField(User)
    song_title=models.CharField(max_length=70)
    duration = models.IntegerField()

    def written_by(self):
        return ','.join([str(p) for p in self.wah.all()])

    