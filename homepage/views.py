from __future__ import unicode_literals

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views import generic,View

from .models import Candidate,Sale
from .forms import CandForm,SalePaymentForm

class CandidateFormView(View):
    model = Candidate
    form_class=CandForm
    template_name='homepage/candidate.html'


    def get(self,request):
        form=self.form_class()
        if not self.request.user.is_staff:
            form.fields.pop('result')
            form.fields.pop('n_attempts')
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if not self.request.user.is_staff:
            form.fields.pop('result')
            form.fields.pop('n_attempts')
        else:
            pass
        if(form.is_valid()):
            form.save()
            return redirect('homepage:cform')
        else:
            pass
        return render(request,self.template_name,{'form':form})


def charge(request):
    if request.method == "POST":
        form = SalePaymentForm(request.POST)

        if form.is_valid():  # charges the card
            return HttpResponse("Success! We've charged your card!")
    else:
        form = SalePaymentForm()

    return render_to_response("homepage/charge.html",
                              RequestContext(request, {'form': form}))