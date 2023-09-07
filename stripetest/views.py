from django.conf import settings
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
STRIPE_TEST_PUBLISHABLE_KEY = settings.STRIPE_TEST_PUBLISHABLE_KEY

def pay(request):
    return render(request, 'pay.html', {'stripe_key': STRIPE_TEST_PUBLISHABLE_KEY})


def charge(request):

    if request.method == 'POST':
        # стоимость берем из скрытой формы data-amount в шаблоне
        amount = int(request.POST['data-amount'])
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )

        return render(request, 'charge.html')