from django import forms

class ExpectadorForm(forms.Form):
    nome = forms.CharField(max_length=100, label='NOME')
    cpf = forms.CharField(max_length=11, label='CPF')
    meia = forms.BooleanField(required=False, label='MEIA ENTRADA')