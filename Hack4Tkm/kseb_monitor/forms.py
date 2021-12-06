from .models import PredictModel
from django.forms import ModelForm
class MyPredictModel(ModelForm):
    class Meta:
        model = PredictModel
        fields = ['Time']