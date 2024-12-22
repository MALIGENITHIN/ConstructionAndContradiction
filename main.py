from django.contrib import admin

from cc.models import UserModel, RatingModel, CommentModel, ConstructionModel, ConstructionRequestModel, ProjectModel

admin.site.register(UserModel)
admin.site.register(RatingModel)
admin.site.register(CommentModel)
admin.site.register(ConstructionModel)
admin.site.register(ConstructionRequestModel)
admin.site.register(ProjectModel)
from django.db import models
from django.db.models import Model
                                                                                
# Create your models here.
class UserModel(Model):

    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    usertype = models.CharField(max_length=50)

    class Meta:
        db_table = "registration model"
class RatingModel(models.Model):

    userid=models.CharField(max_length=60)
    contractorid=models.CharField(max_length=60)
    rating=models.CharField(max_length=60)

    class Meta:
        db_table = "rating"

class CommentModel(models.Model):

    comment = models.TextField(max_length=300)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)
    userid = models.CharField(max_length=60)

    class Meta:
        db_table = "comment"
class ConstructionModel(models.Model):

    date = models.DateTimeField(auto_now=True, blank=False, null=False)
    description=models.CharField(max_length=60)
    housemodel= models.CharField(max_length=500)
    cement= models.CharField(max_length=500)
    sanitaryware= models.CharField(max_length=500)
    hardware= models.CharField(max_length=500)
    iron= models.CharField(max_length=500)
    constructionarea= models.CharField(max_length=500)
    houseplan= models.FileField(upload_to="images")
    userid=models.CharField(max_length=60)


    class Meta:
        db_table = "construction"
class ConstructionModel(models.Model):

    date = models.DateTimeField(auto_now=True, blank=False, null=False)
    description=models.CharField(max_length=60)
    housemodel= models.CharField(max_length=500)
    cement= models.CharField(max_length=500)
    sanitaryware= models.CharField(max_length=500)
    hardware= models.CharField(max_length=500)
    iron= models.CharField(max_length=500)
    constructionarea= models.CharField(max_length=500)
    houseplan= models.FileField(upload_to="images")
    userid=models.CharField(max_length=60)


    class Meta:
        db_table = "construction"
    date = models.DateTimeField(auto_now=True, blank=False, null=False)
    description=models.CharField(max_length=60)
    housemodel= models.CharField(max_length=500)
    cement= models.CharField(max_length=500)
    sanitaryware= models.CharField(max_length=500)
    hardware= models.CharField(max_length=500)
    iron= models.CharField(max_length=500)
    constructionarea= models.CharField(max_length=500)
    houseplan= models.FileField(upload_to="images")
    userid=models.CharField(max_length=60)


    class Meta:
        db_table = "construction"
class ConstructionRequestModel(models.Model):

    constructionid=models.CharField(max_length=60)
    contractorid=models.CharField(max_length=60)
    userid = models.CharField(max_length=60)
    userdescription= models.CharField(max_length=60)
    contractorprice=models.CharField(max_length=60)

    class Meta:
        db_table = "construction request"


class ProjectModel(models.Model):

    userid=models.CharField(max_length=60)
    projectname= models.CharField(max_length=500)
    location= models.CharField(max_length=500)
    image= models.FileField(upload_to="images")
    date = models.DateTimeField(auto_now=True, blank=False, null=False)
