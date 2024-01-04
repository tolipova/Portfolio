from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name="kategoriya nomi")

    def __str__(self):
        return self.category
class Author(models.Model):
    author = models.CharField(max_length=255, verbose_name="author ismi")
    def __str__(self):
        return self.author
    
class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="kategoriyasi nomi")
    project_name = models.CharField(max_length=255, verbose_name="loyiha nomi")
    image = models.ImageField(upload_to='user_info/', verbose_name="loyiha rasmi")
    project_info = models.TextField(verbose_name="qisqacha tafsiloti")
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="author ismi")
    hashteg = models.CharField(max_length=255, verbose_name="post hashtegi")

    def __str__(self) -> str:
        return self.project_name