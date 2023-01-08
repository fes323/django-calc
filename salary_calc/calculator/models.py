from django.db import models


class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100, verbose_name='Квалификация')
    precent = models.IntegerField(default=12, verbose_name='Процент от продаж')
    salary = models.IntegerField(default=37500, verbose_name='Оклад')

    def __str__(self):
        return self.qualification_name

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификации'