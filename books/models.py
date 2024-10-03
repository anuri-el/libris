from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('Author',on_delete=models.CASCADE, null=True, blank=True)
    # genre = models.ManyToManyField('Genre')
    isbn = models.CharField(max_length=17, unique=TabError)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    publication_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # series = model.
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birthdate = models.DateField(null=True, blank=True)
    deathdate = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    