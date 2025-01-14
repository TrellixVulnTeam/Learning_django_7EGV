from django.db import models
from django.contrib.auth.models import User #for usr authentication
from django.utils.timezone import now
# from django.contrib.postgres.fields import JSONField
from jsonfield import JSONField
# Create your models here.

User_status=((0,"Inactive"),(1,"Active"),) #creating  choices for the active/inactive status of user 

class Common_info(models.Model):
    active=models.IntegerField(default=1, choices=User_status)
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    class Meta:# we don't need Common_info to created as a table in database so we use abstract=True
        abstract=True


class RoleType(Common_info):#model for collecting the data of different roletypes
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class UserRole(Common_info):#common_info as a base class  and table for the userroles
    user1=models.OneToOneField(User,on_delete=models.CASCADE)
    roles=models.ManyToManyField(RoleType)
    def __str__(self):
        return self.user1.username


class UserDetail(Common_info):
    website=models.CharField(max_length=50)
    mail=models.EmailField(max_length=50)
    name=models.CharField(max_length=50)
    phonenumber=models.BigIntegerField()
    class Meta:
        db_table="userdetail"
    
    def __str__(self):
        return self.name,self.mail

# model for the queston fieldfrom django.forms import fields, util

class Question(Common_info):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

#choice model
class Choice(Common_info):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    Choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.Choice_text


class School(models.Model):
    SchoolName=models.CharField(max_length=50)
    Address=models.TextField(max_length=100)
    Details=JSONField(default={})

    def __str__(self):
        return self.SchoolName
class School_post(models.Model):
    published_date=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=500)
    school_name=models.ForeignKey(School,related_name="school_post")
    
    def __str__(self):
        return self.content

class Car_brand(models.Model):
    BrandName=models.CharField(max_length=20,verbose_name="Car Brand Name")
    customer_service_number=models.BigIntegerField(verbose_name="customer care number")
    head_quarters=models.CharField(max_length=100)
    CEO=models.CharField(max_length=30)
    
    def __str__(self):
        return self.BrandName

class Car_brand_model(models.Model):
    model_details=JSONField(default={})
    model_id=models.ForeignKey(Car_brand,related_name="model_name")

    def __str__(self):
        for key,values in self.model_details.items():
            return key

