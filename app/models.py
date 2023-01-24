from django.db import models

# Create your models here.
class Dept(models.Model):
    ID = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=30)
    empno = models.IntegerField()

    def __str__(self):
        return self.dname

class Emp(models.Model):
    EID = models.IntegerField(primary_key=True)
    MGR = models.IntegerField()
    ENAME = models.CharField(max_length=50)
    deptno = models.ForeignKey(Dept, on_delete=models.CASCADE)
    sal = models.FloatField()
    hiredate = models.DateField()
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.ENAME

    #def __str__(self):
    #    return self.position