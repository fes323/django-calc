from django import forms
from .models import Qualification

class CalcForm(forms.Form):
    qualification = forms.IntegerField(label='Процент от продажи')
    quantity = forms.IntegerField(label='количество продаж')
    deal_1 = forms.IntegerField(label='Сделка №1')

    deal_2 = forms.IntegerField(label='Сделка №2')
    deal_3 = forms.IntegerField(label='Сделка №3')
    deal_4 = forms.IntegerField(label='Сделка №4')
    deal_5 = forms.IntegerField(label='Сделка №5')
    deal_6 = forms.IntegerField(label='Сделка №6')

