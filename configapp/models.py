from django.db import models

class Avtosalon(models.Model):
    title=models.CharField(max_length=50)
    context=models.TextField()
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=60)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/')
    def __str__(self):
        return self.title


class Brand(models.Model):
    title=models.CharField(max_length=50)
    create_ed=models.DateTimeField(auto_now_add=True)
    update_ed=models.DateTimeField(auto_now_add=True)
    context=models.TextField()
    def __str__(self):
        return self.title

class Car(models.Model):
    salon=models.ForeignKey(Avtosalon,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    model=models.CharField(max_length=20)
    price=models.IntegerField()
    year=models.DateTimeField()
    color=models.CharField(max_length=10)
    def __str__(self):
        return f"{self.model}"