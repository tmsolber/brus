from django import forms

class DepositForm(forms.Form):
    deposit_amount = forms.IntegerField(label='kr', min_value=0)

class AddNameForm(forms.Form):
    add_person = forms.CharField(label='navn', max_length=20)
