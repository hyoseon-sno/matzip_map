from django.db import models

class restaurant(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=10)
    category=models.CharField(max_length=10)
    long=models.FloatField()
    lat=models.FloatField()
    number = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True)

    class Meta:
        db_table='restaurant'

#회원정보
class User(models.Model):
  email = models.CharField(max_length=20)
  name = models.CharField(max_length=20)
  pwd = models.CharField(max_length=20)
  pwd = models.CharField(max_length=20,null=True)

#게시판
class Article(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.CharField(max_length=100, null=True) #게시판 카테고리 변수