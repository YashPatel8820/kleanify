from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Comp(models.Model):
    cn = models.CharField(max_length=50, verbose_name='Company_Name')

    def __str__(self):
        return str(self.cn)

class Plo(models.Model):
    company = models.ForeignKey(Comp, on_delete=models.CASCADE,null=True,blank=True)
    Buyer_data = models.CharField(max_length=50)
    In = models.CharField(max_length=50, verbose_name="Invoice Number", unique=True)
    In_date = models.CharField(max_length=50, verbose_name="Invoice Date", default ='')
    C = models.CharField(max_length=50, verbose_name="State Code", default ='')
    T = models.CharField(max_length=50, verbose_name="Total", default ='')
    G = models.CharField(max_length=50, verbose_name="GST Toal",default ='' )
    file = models.FileField(upload_to='in/',default='', null=True, blank = True)
    ipp = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return str(self.Buyer_data)

class Tally(models.Model):
    company = models.ForeignKey(Comp, on_delete=models.CASCADE,null=True)
    Buyer_data = models.CharField(max_length=50)
    In = models.CharField(max_length=50, verbose_name="Invoice Number", )
    date = models.DateField(verbose_name=" Dated", null = True)
    S = models.CharField(max_length=50, verbose_name="SGST", default ='')
    C = models.CharField(max_length=50, verbose_name="CGST",default ='')
    T = models.CharField(max_length=50, verbose_name="Total",default ='')
    
    file = models.FileField(upload_to='in/',default='',)

    def __str__(self):
        return str(self.Buyer_data)

    

class data(models.Model):
    Paisa = models.IntegerField(null=True, verbose_name= "Price")
    Vastu = models.CharField(max_length=20, verbose_name= "Biscuit_Name", null= True, blank = True, default = None )

    def __str__(self):
        return str(self.Vastu)
