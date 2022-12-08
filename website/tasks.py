from celery import shared_task
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# @shared_task
# def send_mail_to_email(email, phone_number, content):
#     data = {
#         "email": email,
#         'content': content,
#         'phone_number': phone_number
#         # 'phone_number': phone_number
#     }
#     html_body = render_to_string('booknow.html', data)
#     msg = EmailMultiAlternatives(subject='ТИЛЯ ЧОРТ!!', to=[email])
#     msg.attach_alternative(html_body, 'text/html')
#     msg.send()
#     print(msg)

@shared_task
def send_mail_to_email(name, phone, email, address, schedule, date, message):
    data = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address,
        'schedule': schedule,
        'date': date,
        'message': message,
    }
    html_body = render_to_string('h.html', data)
    msg = EmailMultiAlternatives(subject='егег!!', to=[email])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()
    print(msg)
