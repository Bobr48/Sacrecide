from django.urls import reverse
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from datetime import date
from pyexpat.errors import messages
from .models import Concerts, Musicians, History, Foto, Merch, Purchase


# Create your views here.
class SacrecideHome(TemplateView):
    template_name = 'home.html'
    title_page = "Sacrecide band"
    now = date.today()
    data_concert = Concerts.published.filter(date_concert__gt=(now))
    #data_concert = Concerts.published.all()
    extra_context = {
        'title': title_page,
        'concerts': data_concert
    }
    #context_object_name = 'posts'



class Sacrecideabout(TemplateView):
    template_name = 'about.html'
    musicians = Musicians.published.all()
    title_page = 'О группе'
    extra_context = {
        'title': title_page,
        'musicians': musicians,
    }


class Sacrecidepast(TemplateView):
    template_name = 'past.html'
    past = History.published.all()
    title_page = 'Произошедшее'
    fotos = Foto.objects.all()
    extra_context = {
        'title': title_page,
        'past': past,
        'photo': fotos

    }
class Sacrecidemerch(TemplateView):
    template_name = 'merch.html'
    items = Merch.published.all()
    title_page = 'Мерч'
    extra_context = {
        'title': title_page,
        'items': items,
    }


class Sacrecidebuy(CreateView):
    fields = ['quantity','name', 'patronymic','surname', 'address','phone','size']
    id_for_foto = None
    template_name = 'buy.html'
    model = Purchase
    title_page = 'Мерч'
    extra_context = {
        'title': title_page,
        'id_product': id_for_foto,
    }

    def form_valid(self, form):
        form.instance.item_id = self.kwargs['id_product']
        self.id_for_foto = self.kwargs['id_product']
        form.instance.name_product = Merch.published.filter(id=self.kwargs['id_product']).first()
        print('form_valid')
        return super(Sacrecidebuy, self).form_valid(form)

    def get_success_url(self):
        print('get_success_url', self.kwargs['id_product'])
        return reverse('send')


def send_email(request):
    data = Purchase.objects.latest()
    message = (f"Произведена покупка {data.name_product}, в количестве {data.quantity}, Размер: {data.size}. Покупатель: {data.name} {data.patronymic} {data.surname}. "
               f"Адрес: {data.address}. Телефон: {data.phone}")
    print(message)
    email = EmailMessage(str('Покупка' + data.name_product), message, to=['bobrovskaleksej73@gmail.com'])
    email.send()
    response = redirect('home')
    return response

#рабоч
    # def get_success_url(self):
    #     return reverse('buy', kwargs={'id_product': self.kwargs['id_product']})



        # quantity
        # name
        # patronymic
        # surname
        # address
        # phone
        # pay
        # size
        # data
        # email = EmailMessage(str('Покупка' + self.name_product), 'Body', to=['bobrovskaleksej73@gmail.com'])
        # email.send()