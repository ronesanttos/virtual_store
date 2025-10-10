import requests
from django import forms
from django.core.exceptions import ValidationError

class EnderecoForm(forms.Form):
    cep = forms.CharField(label="CEP", max_length=9)

    def clean_cep(self):
        cep = self.cleaned_data['cep'].replace('-', '').strip()

        if len(cep) != 8 or not cep.isdigit():
            raise ValidationError("CEP deve conter 8 dígitos numéricos.")

        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code != 200:
            raise ValidationError("Erro ao consultar o CEP.")

        data = response.json()

        if data.get('erro'):
            raise ValidationError("CEP não encontrado.")

        # Armazena os dados do endereço no form para uso posterior
        self.cleaned_data['logradouro'] = data.get('logradouro')
        self.cleaned_data['bairro'] = data.get('bairro')
        self.cleaned_data['cidade'] = data.get('localidade')
        self.cleaned_data['uf'] = data.get('uf')

        return cep
