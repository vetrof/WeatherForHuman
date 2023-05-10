from django.forms import Form


class FeelForm(Form):
    class Meta:
        fields = ('feel', 'info')
