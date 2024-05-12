from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EmployeeDetail(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    empid=models.CharField(max_length=50,null=True)
    stafftype=models.CharField(max_length=10, default="Teaching Staff")

    DOB=models.DateField(max_length=50,null=True)
    altemail=models.CharField(max_length=50,null=True)
    mob=models.CharField(max_length=10,null=True)
    altmob=models.CharField(max_length=10,null=True)
    gender=models.CharField(max_length=50,null=True)
    adhar=models.CharField(max_length=50,null=True)
    pan=models.CharField(max_length=50,null=True)
    mstatus=models.CharField(max_length=50,null=True)
    bloodgroup=models.CharField(max_length=50,null=True)
    joiningdate=models.DateField(max_length=50,null=True)
    worklocation=models.CharField(max_length=50,null=True)
    workexperience=models.CharField(max_length=50,null=True)
    presenthousenum=models.CharField(max_length=50,null=True)
    presentstreet=models.CharField(max_length=50,null=True)
    presentcity=models.CharField(max_length=50,null=True)
    presentdist=models.CharField(max_length=50,null=True)
    presentstate=models.CharField(max_length=50,null=True)
    presentzip=models.CharField(max_length=50,null=True)
    curhousenum=models.CharField(max_length=50,null=True)
    curstreet=models.CharField(max_length=50,null=True)
    curcity=models.CharField(max_length=50,null=True)
    curdist=models.CharField(max_length=50,null=True)
    curstate=models.CharField(max_length=50,null=True)
    curzip=models.CharField(max_length=50,null=True)
    def __str__(self):
        #return self.firstname
        return self.user.username

class NonTeachingEmployee(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #empid=models.CharField(max_length=50,null=True)
    
    dept=models.CharField(max_length=50,null=True)
    

    noe10=models.CharField(max_length=50,null=True)
    board10=models.CharField(max_length=50,null=True)
    marks10=models.IntegerField(default=0)
    yop10=models.DateField(max_length=50,null=True)

    noe12=models.CharField(max_length=50,null=True)
    board12=models.CharField(max_length=50,null=True)
    marks12=models.IntegerField(default=0)
    yop12=models.DateField(max_length=50,null=True)

    noedegree=models.CharField(max_length=50,null=True)
    uni=models.CharField(max_length=50,null=True)
    marksdeg=models.IntegerField(default=0)
    yopdeg=models.DateField(max_length=50,null=True)
    desg=models.CharField(max_length=50,null=True)
    
    
    
    
    def __str__(self):
        #return self.firstname
        return self.user.username
    
class TeachingEmployee(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #empid=models.CharField(max_length=50,null=True)
    
    dept=models.CharField(max_length=50,null=True)
    

    noe10=models.CharField(max_length=50,null=True)
    board10=models.CharField(max_length=50,null=True)
    marks10=models.IntegerField(default=0)
    yop10=models.DateField(max_length=50,null=True)

    noe12=models.CharField(max_length=50,null=True)
    board12=models.CharField(max_length=50,null=True)
    marks12=models.IntegerField(default=0)
    yop12=models.DateField(max_length=50,null=True)

    noedegree=models.CharField(max_length=50,null=True)
    uni=models.CharField(max_length=50,null=True)
    marksdeg=models.IntegerField(default=0)
    yopdeg=models.DateField(max_length=50,null=True)
    
    npg=models.CharField(max_length=50,null=True)
    unipg=models.CharField(max_length=50,null=True)
    markspg=models.IntegerField(default=0)
    yoppg=models.DateField(max_length=50,null=True)


    unidoc=models.CharField(max_length=50,null=True)
    stramdoc=models.CharField(max_length=50,null=True)
    dreg=models.DateField(max_length=50,null=True)
    yopdoc=models.DateField(max_length=50,null=True)

    unipdoc=models.CharField(max_length=50,null=True)
    strampdoc=models.CharField(max_length=50,null=True)
    stdate=models.DateField(max_length=50,null=True)
    enddate=models.DateField(max_length=50,null=True)




    
    desg=models.CharField(max_length=50,null=True)

    
    
    def __str__(self):
        #return self.firstname
        return self.user.username
