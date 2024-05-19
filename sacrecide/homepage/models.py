import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        # for i in super().get_queryset().filter(date_concert=1):
        #     print (i)
        return super().get_queryset().filter(is_published=Concerts.Status.PUBLISHED)


class Concerts(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'


    date_concert = models.DateTimeField()
    city = models.CharField(max_length=255, verbose_name='Город')
    place = models.CharField(max_length=255, verbose_name='Место')
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cost = models.CharField(max_length=12, verbose_name='Цена', default='')
    url_ticket = models.CharField(max_length=255, verbose_name='Ссылка на покупку билетов',default=None, blank=True, null=True,)
    objects = models.Manager()
    published = PublishedManager()



    def __str__(self):
        return str(self.place)

    class Meta:
        ordering = ['date_concert']
        indexes = [models.Index(fields =['date_concert'])]



class Musicians(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")
    name = models.CharField(max_length=255, verbose_name='Имя')
    text = models.TextField(max_length=2550, verbose_name='Текст')
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()



    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields =['name'])]




class History(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(max_length=2550, verbose_name='Текст')
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    slug = models.SlugField(max_length=255, blank=True, db_index=True, default='')
    time = models.DateTimeField()


    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['time']
        indexes = [models.Index(fields =['time'])]


class Foto(models.Model):
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")
    owner = models.ForeignKey('History', on_delete=models.PROTECT, related_name='fotos')
    name = models.CharField(max_length=255, verbose_name='Название', null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={"photo": self.photo})

class Merch(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")
    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(max_length=2550, verbose_name='Текст')
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cost = models.IntegerField(null=True)
    published = PublishedManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('buy', kwargs={'id_product': self.pk})

class Purchase(models.Model):

    def convertDatetimeToString(o):
        DATE_FORMAT = "%Y-%m-%d"
        TIME_FORMAT = "%H:%M:%S"

        if isinstance(o, datetime.date):
            return o.strftime(DATE_FORMAT)
        elif isinstance(o, datetime.time):
            return o.strftime(TIME_FORMAT)
        elif isinstance(o, datetime.datetime):
            return o.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))

    sizes = [
        ('S', "S"),
        ('M', "M"),
        ('L', "L"),
        ('XL', "XL"),
        ('XXL', "XXL"),
    ]
#
    name_product = models.CharField(max_length=255, null=True, verbose_name="Название товара")
    quantity = models.IntegerField(null=True, verbose_name="Количество")
    name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    address = models.CharField(max_length=255, verbose_name='Адрес пункта выдачи СДЕК')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    pay = models.BooleanField(default=False, verbose_name='Оплата')
    size = models.CharField(max_length=4, choices=sizes, verbose_name='Размер')
    data = models.DateTimeField(auto_now=True, verbose_name='Дата покупки')

    item = models.ForeignKey('Merch', on_delete=models.PROTECT, related_name='items', null=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-data']
        indexes = [models.Index(fields =['data'])]
        get_latest_by = 'data'

    def __str__(self):
        return self.name_product

    def get_absolute_url(self):
        return reverse('home')

  # Первый параметр - имя вашего маршрута, например path('', views.index, name="car")
