from django.db import models

# Create your models here.

class productsdetails(models.Model):
    CATEGORY_CHOICES = [
        ('NoteBooks', 'NoteBooks'),
        ('Pens', 'Pens'),
        ('Pencils', 'Pencils'),
        ('Dairy', 'Dairy'),
        ('Tape', 'Tape'),
        ('Sheets', 'Sheets'),
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shopimages')
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default= 'NoteBooks')

    def __str__(self):
        return self.name