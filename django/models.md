# Django
### Introduction
Much of this is taken from various tutorials, like the youtube one by @thenewboston which creates a music store(?) app.

### Some of my aliases
```bash
pdm      		 	// python manage.py
pdm r   		 	// python manage.py runserver
pdm app app_name 	// python manage.py startapp app_name
pdm <other_command> // python manage.py other_command
```

### Making a new model
Add this to the root settings.py file.

```python
INSTALLED_APPS = [
    'music.apps.MusicConfig',
    ...
]
```

Where...
- “music” is the app directory name,
- “apps” is the apps.py file
- “MusicConfig” is the function declared in the apps.py file.

Which means you need to create the app class MusicConfig

apps.py
```python
from django.apps import AppConfig

class MusicConfig(AppConfig):
    name = 'music'

```

Obviously you need to create the Models...

models.py
```python
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + " - " + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
```


If you want to manage the models in your admin panel, register it.

admin.py
```python
from django.contrib import admin
from .models import Album, Song

admin.site.register(Album)
admin.site.register(Song)
```


When you change a model you need to make the migration, then apply it

```bash
// Create the migration number. 
pdm makemigrations music
//optional, shows details of migration number created from above
pdm sqlmigrate music 0001
// Runs migration
pdm migrate 
```

### Creating and querying
```bash
pdm shell
>>> From music.models import Album, Song
>>> a = Album(artist="Aaron", album_title="red",genre="rock",album_logo=“www.urlasdf.com”)
>>> a.save()
>>> Album.objects.all()
<QuerySet [<Album: Album object>]>
>>> a.id
1
>>> a.pk
1
>>> Album.objects.filter(id=1)
>>> Album.objects.filter(artist__startswith=“Aaron”)

// create songs from Django shell
>>> album1.song_set.create(song_title="another title", file_type="mp3”)
>>> all_songs = album1.song_set.all()
>>> all_songs[0]
<Song: the coolest title>
```

#### Creating a super User
```bash
pdm su // alias of: python manage.py createsuperuser
```

### Templates
Create index.html or whatever
```
<p>
  {% python code in here %}
  {{ request variable here }}
</p>
```