from django.db import models

# Create your models here.
class ledger(models.Model):
    Buyer_data = models.CharField(max_length=50)
    In = models.CharField(max_length=50, verbose_name="Invoice Number")
    In_date = models.CharField(max_length=50, verbose_name="Invoice Date")
    C = models.CharField(max_length=50, verbose_name="State Code")
    T = models.CharField(max_length=50, verbose_name="Total")
    G = models.CharField(max_length=50, verbose_name="GST Toal")

    def __str__(self):
        return str(self.Buyer_data)


