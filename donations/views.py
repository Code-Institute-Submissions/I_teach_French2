from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


import stripe


# Create your views here.

def donations(request):

    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1IZeB1H1ShqjMsUgKO2mxnrp',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('donations')),
        # success_url= "https://8000-amber-anglerfish-it1rj2m4.ws-eu03.gitpod.io/donations/success" + '?session_id={CHECKOUT_SESSION_ID}',
        # cancel_url= "https://8000-amber-anglerfish-it1rj2m4.ws-eu03.gitpod.io/donations/",
    )

    context ={
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    }

    return render(request, 'donations.html', context)


def success(request):
    return render(request, 'success.html')

def checkout(request):
    return render(request, 'success.html')
