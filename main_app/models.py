from django.db import models

from datetime import date

from django.urls import reverse

RATING = (
    (5, '5 stars'),
    (4, '4 stars'),
    (3, '3 stars'),
    (2, '2 stars'),
    (1, '1 star')
)

class Award(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('awards_detail', kwargs={'pk': self.id})

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    description = models.TextField(max_length=250)
    awards = models.ManyToManyField(Award)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Review(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('date')
    rating = models.IntegerField(
        choices=RATING,
        default=RATING[0][0]
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"
