from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"

    #form_class attribute that allpow us to create objects
    form_class = UserCreationForm
    success_url = reverse_lazy("login")