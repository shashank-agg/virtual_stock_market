from .models import UserProfile
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('balance',)

class BuyAndSellForm(forms.ModelForm):
	SellStocksCount = forms.IntegerField(initial=0, label='No. of stocks to sell')
	BuyStocksCount = forms.IntegerField(initial=0, label='No. of stocks to buy')
	class Meta:
		model = UserProfile
		fields = ()
