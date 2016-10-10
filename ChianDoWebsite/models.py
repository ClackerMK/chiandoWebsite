from django.db import models


# Blog Eintrag
from django.utils import timezone


class Blog(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    pinned = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    thumbnail = models.ForeignKey("Picture", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# Termin (eine Art von Blog Eintrag)
class Event(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    place = models.TextField(blank=True)
    gps_lon = models.FloatField(null=True, blank=True)
    gps_lat = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.blog.name

# Eine Gallerie von Bildern (eine Art von Blog Eintrag)
class Gallery(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.blog.name

# Einzelnes Bild (nicht unbedingt Teil einer Galerie)
class Picture(models.Model):
    path = models.ImageField(upload_to="images")
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return self.path.url

# Einzelnes Bild (Teil einer Galserie)
class GalleryPicture(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    picture = models.OneToOneField(Picture, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.picture.path.url
