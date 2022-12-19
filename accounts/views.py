from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm
from django.utils.encoding import force_text
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, View
from django.utils.translation import gettext as _
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from accounts.confirm_email.tasks import send_confirmation_mail
from accounts.confirm_email.tokens import account_activation_token

from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from verify_email import verify_email


User = get_user_model()


class loginView(View):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def get(self, request):
        form = self.form_class
        return render (request, self.template_name, {'form': form,})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            if user := authenticate(username=username, password=password):
                messages.success(request,f'You are logged in as {username}')
                login(request, user)
                return redirect('/')
        else:
            messages.error(request, _('Included information is false! Please enter right username and password!'))
            return render(request, 'login.html', {'form': form})


class register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        result = super().form_valid(form)
        form.instance.username = self.request.user
        send_confirmation_mail(user=self.object, current_site=get_current_site(self.request))
        return result
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     send_confirmation_mail(user=self.object, current_site=get_current_site(self.request))
    #     return result
    # def form_valid(self, form):
    #     form.instance.username = self.request.user
    #     # form.instance.save()
    #     return super().form_valid(form)
    

class ActivateAccountView(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Your account is activated!")
            return redirect(reverse_lazy('login'))
        else:
            messages.warning(request, "Something went wrong!")
            return redirect(reverse_lazy('login'))


class Logout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))

