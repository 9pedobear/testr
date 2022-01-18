from django.db import models

# Create your models here.
class Employes(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=10)

    class Meta:
        db_table = 'Сотрудники'
