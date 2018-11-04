from django.db import models
from django.utils import timezone
from django.contrib import admin

class Tropa(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    valor = models.IntegerField()

    def add(self):
        self.save()

    def __str__(self):
        return self.nombre

class Arena(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.IntegerField()
    tropas = models.ManyToManyField(Tropa, through='Ejercito')

    def add(self):
        self.save()

    def __str__(self):
        return self.nombre

class Ejercito(models.Model):
    tropa = models.ForeignKey(Tropa, on_delete=models.CASCADE)
    arena = models.ForeignKey(Arena, on_delete=models.CASCADE)

class EjercitoInLine(admin.TabularInline):
    model = Ejercito
    extra = 1

class TropaAdmin(admin.ModelAdmin):
    inlines = (EjercitoInLine,)

class ArenaAdmin(admin.ModelAdmin):
    inlines = (EjercitoInLine,)
