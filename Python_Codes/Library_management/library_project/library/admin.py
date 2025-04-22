from django.contrib import admin

# Register your models here.
from .models import Author, Book, Member
# Registering all models to show in Django admin
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Member)