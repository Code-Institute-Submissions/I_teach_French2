from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

import stripe

# Create your views here.

stripe.api_key = "sk_test_51IZFBcH1ShqjMsUgbj196eJgRVCJjJeUh5nvS8yHaaqJ2LwJ4GY2rbGB97M1AbpN3IMoZYrAa1ypIFfJiacFCrFc00HgZmyYxE"

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


