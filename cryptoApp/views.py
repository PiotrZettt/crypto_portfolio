import json

from django.shortcuts import render, redirect
from binance.spot import Spot
from .forms import ConnectForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """
    Create a Binance client using an api_key and secret_key retrieved
    from connect_to_binance form.
    Get all the basic account info with the account() method.
    Pass the context to render in index.html
    """

    api = request.session.get('api_key')
    secret = request.session.get('secret_key')

    client = Spot(key=api, secret=secret)

    account_info = client.account()
    data = json.dumps(account_info)
    loaded_data = json.loads(data)
    balances = loaded_data['balances']

    active_assets = []
    current_value = 0.0
    worth = 0.0

    for item in balances:
        if item['free'] not in ['0.00000000', '0.00', '0.0']:
            asset = item['asset']
            get_price = client.ticker_price(asset + 'USDT')
            price = round(float(get_price['price']), 2)
            current_value = round(float(item['free']) * price, 2)
            worth += current_value
            active_assets.append(
                {'asset': asset,
                'available': item['free'],
                'price': price,
                'current_value': current_value})


    context = {
        'assets': active_assets,
        'current_value': current_value,
        'worth': worth
    }
    return render(request, 'index.html', context)

def connect_to_binance(request):
    """
    Render a form and pass the api_key and secret_key input to request.session
    """

    form = ConnectForm()

    if request.method == 'POST':
        form = ConnectForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            secret_key = form.cleaned_data['secret_key']

            request.session['api_key'] = api_key
            request.session['secret_key'] = secret_key

            return redirect('index')
    return render(request, 'connect.html', {'form': form})

