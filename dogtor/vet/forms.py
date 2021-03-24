# from django import forms
# from .models import PetOwner

# class OwnerForm(forms.Form): # esto da el comportamiento de formulario a OwnerForm
#     class Meta:
#         model = PetOwner
#         first_name  = forms.CharField()
#         last_name   = forms.CharField()
#         address     = forms.CharField()
#         email       = forms.CharField()
#         phone       = forms.CharField()

#     def send_email(self):
#         # send email using the self.cleaned_data dictionary
#         pass

from django import forms

from .models import PetOwner, Pet


class OwnerForm(forms.ModelForm):
    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "address", "email", "phone"]
        # widgets = {"email ": forms.EmailInput()}
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Pon tu nombre", "class": "clase-custom"}
            )
        }

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "type", "owner"]
        widgets = {"email ": forms.EmailInput()}