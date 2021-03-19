from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
#from django.views.generic.edit import 
from django.urls import reverse_lazy

from .models import PetOwner, Pet
from vet.forms import OwnerForm

# Create your views here.
# class Owners(View):
#     def get(self, request):
#         owners = PetOwner.objects.all()
#         context = {"owners": owners}

#         template = loader.get_template("vet/owners/list.html")
#         return HttpResponse(template.render(context, request))

# class PetsDetail(View):
#     def get(self, request,pk):
#         pet = Pet.objects.get(id=pk)
#         context = {"pet": pet}

#         template = loader.get_template("vet/pets/detail.html")
#         return HttpResponse(template.render(context, request))

# class PetsList(TemplateView):
#     template_name = "vet/pets/list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context, "ESTO VIENE DEL PADRE (TEMPLATEVIEW)")
#         context["pets"] = Pet.objects.all()
#         print(context, "ESTO LE AGREGAMOS NOSOTROS")
#         return context

class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"


class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"

class OwnersCreate(CreateView):
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")   # vet es mascarilla
    # ver http://127.0.0.1:8000/vet/owners/add/
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

class PetsList(ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"

class PetsDetail(DetailView):
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"