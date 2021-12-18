from django import forms
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
 
# modelos do formulario de contato
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    # funcao que envia email mail
    def send_mail(self): 
        email = self.cleaned_data['email'] 
  
        subject = 'E-mail enviado django'
        html_message = render_to_string('sendmail.html')
        plain_message = strip_tags(html_message)
        from_email='seu email'
        to= email

        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
