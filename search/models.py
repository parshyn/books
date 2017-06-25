from django.db import models


class Book(models.Model):
    class Meta:
        db_table = 'book'
    title = models.CharField(max_length=300)
    table_of_content = models.TextField()


class Page(models.Model):
    class Meta:
        db_table = 'page'
    number = models.IntegerField()
    chapter = models.IntegerField()
    content = models.TextField()
    book_id = models.ForeignKey(Book)

