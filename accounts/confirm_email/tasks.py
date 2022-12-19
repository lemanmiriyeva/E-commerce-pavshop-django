from django.conf import settings
from  django.core.mail import EmailMultiAlternatives
from accounts.confirm_email.tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

def send_confirmation_mail(user, current_site):
    message = render_to_string('confirmation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
    subject = "Please confirm your account"
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[user.email, ])
    mail.content_subtype = 'html'
    mail.send()