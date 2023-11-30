from django import forms
from gym.models import Personal

from .utils import add_placeholder

class PersonalRegister(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            'nome',
            'sobrenome',
            'E_mail',
            'telefone',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['nome'], 'Ex.: João')
        add_placeholder(self.fields['sobrenome'], 'Ex.: Almeida')
        add_placeholder(self.fields['E_mail'], 'Ex.: João@.com')
        add_placeholder(self.fields['telefone'], '(00) 00000-0000')

        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
    
    nome = forms.CharField(
        label='Nome do personal:',
        max_length=20
    )

    sobrenome = forms.CharField(
        label='Sobrenome:',
        max_length=20
    )

    E_mail = forms.EmailField(
        label='E-mail:',
    )

    telefone = forms.CharField(
        label='Telefone:',
    )