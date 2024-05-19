from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, Model, TextField, ImageField, TextChoices, IntegerField, PositiveIntegerField


class Combine(Model):
    class Condition(TextChoices):
        WORKING = 'Рабочий', 'Рабочий'
        NO_WORKING = 'Нерабочий', 'Нерабочий'

    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='media/')
    condition = CharField(max_length=15, choices=Condition.choices, default=Condition.WORKING)

    def __str__(self):
        return self.name


class Tractor(Model):
    class Condition(TextChoices):
        WORKING = 'Рабочий', 'Рабочий'
        NO_WORKING = 'Нерабочий', 'Нерабочий'

    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='media/')
    condition = CharField(max_length=15, choices=Condition.choices, default=Condition.WORKING)

    def __str__(self):
        return self.name


class MineralEndorsements(Model):
    name = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='media/')
    weight = CharField(max_length=25)

    def __str__(self):
        return self.name


class Workers(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    job_title = CharField(max_length=255)
    image = ImageField(upload_to='media/')
    age = PositiveIntegerField()
    salary = IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class OtherEquipments(Model):
    name = CharField(max_length=255)
    quantity = IntegerField()
    condition = IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    pass
