# from django.db import models

# # Create your models here.
# class File(models.Model):
#     id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
#     name = models.CharField(max_length=255)  # Name of the file
#     path = models.CharField(max_length=500)  # File path as a string
#     size = models.BigIntegerField()  # File size in bytes (BigInteger for large files)
#     type = models.CharField(max_length=50)  # File type or extension (e.g., "txt", "pdf")
#     date = models.DateTimeField(auto_now_add=True)  # Auto-set to the current date and time

#     def __str__(self):
#         return self.name  # String representation of the file object

from django.db import models

class File(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    path=models.CharField(max_length=500)
    size=models.BigIntegerField()
    type=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)