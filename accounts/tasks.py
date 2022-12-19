from celery import shared_task
from django.conf import settings
from .models import SubscriberEmail
from product.models import ProductReviewStatic, Product_version
from django.template.loader import render_to_string
from  django.core.mail import EmailMultiAlternatives
import datetime


@shared_task(name='send_mail')
def send_mail_to_subscribers():
    today = datetime.date.today() + datetime.timedelta(1)
    week_ago = today - datetime.timedelta(7)
    email_list = SubscriberEmail.objects.filter(is_active=True).values_list('email', flat=True)
    ids = ProductReviewStatic.objects.filter(created_at__range = [week_ago, today]).values_list('product_version').order_by('-avg_rating')[0:3]
    products = Product_version.objects.filter(id__in = ids)
     
    message = render_to_string('email-subscribers.html', {
                'products': products,
            })
    subject = "Most Review Products"
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'html'
    mail.send()
    print('sended')


@shared_task(name = "print_msg_main")
def print_message(message, *args, **kwargs):
  print(f"Celery is working!! Message is {message}")
