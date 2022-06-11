from django.forms import ModelForm
from . models import Connect

class ConnectForm(ModelForm):
    class Meta:
        model = Connect
        fields = [
            'api_key',
            'secret_key',
        ]

