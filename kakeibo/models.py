from django.db import models

class Expense(models.Model):
    date = models.DateField()
    categorary = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.categorary}: {self.amount}"