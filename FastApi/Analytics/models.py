# from django.db import models
# from django.contrib.auth.models import User 

# # Create your models here.
# class Transaction(models.Model):
#     TRANSACTION_TYPES = (('income' , 'Income'),('expense', 'Expense'))

#     user = models.ForeignKey(User , on_delete=models.CASCADE)
#     title = models.CharField(max_length=20)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
#     category = models.CharField(max_length=20)
#     date = models.DateTimeField()
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#IN ORDER TO USE THE DJANGO CRETAED TABLE FOR OUR FASTAPI THE TABLE NAME AND FIELDS SHOULD BE IDENTICAL TO THE DJANGO MODEL

from .database import Base
from sqlalchemy import Column, String, Integer, Numeric, DateTime, ForeignKey

class Transaction(Base):
    __tablename__ =  'Transacations_transaction'   # In order to use the same table name from djano model transaction using the same table name 
                     #The table name canbe found under the mysqlworkbench and we have to define the fields same as django model
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('auth_user.id'))  #here auth_user is the user table in db check in mysqlworkbench there we can found all the tables
    title = Column(String)
    amount = Column(Numeric)
    transaction_type = Column(String)
    category = Column(String)
    date = Column(DateTime)
    description = Column(String)
    created_at = Column(DateTime)


