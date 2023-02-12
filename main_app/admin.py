from django.contrib import admin

from .models import Book, Review, Award

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Award)