from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre')
    isbn = models.CharField(max_length=13, unique=TabError)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    # publisher = models.
    # rating = models.
    # series = model.
    slug = models.SlugField(unique=True)


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    deathdate = models.DateField(null=True, blank=True)
    slug = models.SlugField(unique=True)



class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)