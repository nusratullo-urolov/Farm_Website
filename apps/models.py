from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, Model, TextField, ImageField, TextChoices, IntegerField, PositiveIntegerField, \
    BooleanField


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


class AdCombine(Model):
    c_name = CharField(max_length=255)
    c_quantity = PositiveIntegerField()
    c_price = PositiveIntegerField()
    c_driver = BooleanField(default=False)
    c_quickly = BooleanField(default=False)

    def __str__(self):
        return self.c_name


class AdTractor(Model):
    t_name = CharField(max_length=255)
    t_quantity = PositiveIntegerField()
    t_price = PositiveIntegerField()
    t_driver = BooleanField(default=False)
    t_quickly = BooleanField(default=False)

    def __str__(self):
        return self.t_name


class AdMineral(Model):
    m_name = CharField(max_length=255)
    m_price = PositiveIntegerField()
    m_weight = PositiveIntegerField()
    m_quickly = BooleanField(default=False)

    def __str__(self):
        return self.m_name


class AdWorker(Model):
    w_name = CharField(max_length=255)
    w_quantity = PositiveIntegerField()
    w_price = PositiveIntegerField()
    w_quickly = BooleanField(default=False)

    def __str__(self):
        return self.w_name


class AdEquipment(Model):
    e_name = CharField(max_length=255)
    e_quantity = PositiveIntegerField()
    e_price = PositiveIntegerField()
    e_quickly = BooleanField(default=False)

    def __str__(self):
        return self.e_name


class AdFarm(Model):
    f_name = CharField(max_length=255)
    f_quantity = PositiveIntegerField()
    f_price = PositiveIntegerField()
    f_quickly = BooleanField(default=False)

    def __str__(self):
        return self.f_name
