from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,auto_created=True,unique=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(max_length=50,auto_created=True,unique=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    teachers = models.ForeignKey(Teacher, null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True,verbose_name='Kurs Adi',help_text='Kurs Adini Giriniz')
    category=models.ForeignKey(Category, null=True , on_delete=models.DO_NOTHING)
    tags=models.ManyToManyField(Tags)
    students=models.ManyToManyField(User,blank=True, related_name='courses_joined')
    description= models.TextField(max_length=500,null=True,verbose_name='Kurs Aciklamasi')
    image= models.ImageField(upload_to='courses/%Y/%m/%d/', default='courses/6306470.jpg')
    created_date=models.DateTimeField(auto_now=True)
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.name