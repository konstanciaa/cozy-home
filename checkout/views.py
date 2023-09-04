from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NhprgIFIPZTaOSpeA2MY3gqOd64ToDua3aZbZ8FCbtULd3fW7LACUGWdWC2TT3UNdieUR4ue42dZLMbYfhDTOPN00Sk7xFeGD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
