from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from value.models import Value
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from value.forms import ValueChoiceForm

class CreateValueView(FormView):
    template_name = 'create_value.html'
    form_class = ValueChoiceForm
    success_url = reverse_lazy('portfolio')

    def post(self, request, *args, **kwargs):

        form = ValueChoiceForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            value = data.getlist('value')
            value = value[0]
            print(value)
            value = Value(user=request.user, value=value)
            value.save()
            return HttpResponseRedirect(reverse('portfolio'))

