from django.db import models

# Create your models here.
def agge():
    sp = []
    for i in range(1, 19):
        sp.append((i, i,))
    return sp
class Child(models.Model):

    first_name = models.CharField(verbose_name='Имя', max_length=20, primary_key=True)
    last_name = models.CharField(verbose_name='Имя', max_length=20)
    age = models.IntegerField(choices=agge())
    parent = models.ForeignKey('Parent', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

class Parent(models.Model):
    name = models.CharField(verbose_name='', max_length=20)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'