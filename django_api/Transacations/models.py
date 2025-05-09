from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPES = (('income' , 'Income'),('expense', 'Expense'))

    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=20)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

