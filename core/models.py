from django.db import models

# Create your models here.

class Emission(models.Model):
    """Emission object"""
    id = models.IntegerField(primary_key=True, null=False)
    date_created = models.DateTimeField("Date Created", null=False)
    accounting_period = models.CharField("Accounting period", max_length=255, null=False)
    scope_1 = models.IntegerField("Scope 1", null=True)
    scope_2 = models.IntegerField("Scope 2", null=True)
    scope_3 = models.IntegerField("Scope 3", null=True)


    def __str__(self) -> str:
        return f"{id} || {self.date_created} || {self.accounting_period}"