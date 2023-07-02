from django import forms 
from relatorioapp.models import Relatorio, Programacao, Carrossel
#from crispy_forms.helper import FormHelper


class RelatorioForm(forms.ModelForm):
    class Meta:
        model = Relatorio
        fields = '__all__'
        widgets = {
            "data": forms.DateInput(attrs={'type': 'date', 'class':'form-control'} ),
            "titulo":forms.TextInput(attrs={'class':'form-control'}),
            "descricao":forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            "tipo":forms.Select(attrs={'class':'form-select'}),
            "autor":forms.TextInput(attrs={'class':'form-control'}),
            "paragrafo1":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "paragrafo2":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "paragrafo3":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "paragrafo4":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "paragrafo5":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "arquivo":forms.FileInput(attrs={'class':'form-control'}),
            "imagem_thumb":forms.FileInput(attrs={'class':'form-control'}),
            "imagem_post":forms.FileInput(attrs={'class':'form-control'}),
            "legenda_imagem":forms.Textarea(attrs={'class':'form-control', 'rows':2}),
            "url":forms.TextInput(attrs={'class':'form-control'}),
        }



class ProgramacaoForm(forms.ModelForm):
    class Meta:
        model = Programacao
        fields = '__all__'
        titulo= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
        widgets = {
            "data": forms.DateInput(attrs={'type': 'date', 'class':'form-control'} ),
            "titulo":forms.TextInput(attrs={'class':'form-control'}),
            "descricao":forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            "tipo":forms.Select(attrs={'class':'form-select'}),
            "autor":forms.TextInput(attrs={'class':'form-control'}),
            "paragrafo1":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "paragrafo2":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "paragrafo3":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "paragrafo4":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "paragrafo5":forms.Textarea(attrs={'class':'form-control', 'rows':8}),
            "arquivo":forms.FileInput(attrs={'class':'form-control'}),
            "imagem_thumb":forms.FileInput(attrs={'class':'form-control'}),
            "imagem_post":forms.FileInput(attrs={'class':'form-control'}),
            "legenda_imagem":forms.Textarea(attrs={'class':'form-control', 'rows':2}),
        }
        # helper = FormHelper()
        def __init__(self, *args, **kwargs):
            super(ProgramacaoForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


class CarrosselForm(forms.ModelForm):
    class Meta:
        model = Carrossel
        fields = '__all__'
        widgets = {
            "imagem":forms.FileInput(attrs={'class':'form-control'}),
            "legenda1":forms.Textarea(attrs={'class':'form-control', 'rows':1}),
            "legenda2":forms.Textarea(attrs={'class':'form-control', 'rows':2}),
        }




#===============================================================
class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)