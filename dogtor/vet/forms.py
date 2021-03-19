from django import forms

class OwnerForm(forms.Form): # esto da el comportamiento de formulario a OwnerForm
    class Meta:
        model = PetOwner
        first_name  = forms.CharField()
        last_name   = forms.CharField()
        address     = forms.CharField()
        email       = forms.CharField()
        phone       = forms.CharField()

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
