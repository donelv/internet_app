from django import forms
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Computer, DisplayClass

def index(request): 
  return render(request, 'index.html')

def report(request):
  computers = Computer.objects.all()
  params = {'computers': computers}
  return render(request, 'report.html', params)

def dispclass_list(request):
  classes = DisplayClass.objects.all().values()
  params = {'entity': 'DisplayClass', 'objects': classes}
  return render(request, 'list.html', params)

def computers_list(request):
  computers = Computer.objects.all().values()
  params = {'entity': 'Computer', 'objects': computers}
  return render(request, 'list.html', params)

class DisplayClassCreate(CreateView):
  model = DisplayClass
  fields = ['room_number', 'square']
  success_url = '/class'
  template_name = 'class_form.html'

class DisplayClassUpdate(UpdateView):
  model = DisplayClass
  fields = ['room_number', 'square']
  pk_url_kwarg = 'disp_id'
  success_url = '/class'
  template_name = 'class_form.html'

class DisplayClassDelete(DeleteView):
  model = DisplayClass
  pk_url_kwarg = 'disp_id'
  success_url = '/class'
  template_name = 'class_delete_form.html'

class ComputerCreate(CreateView):
  model = Computer
  fields = ['cpu', 'graphic_card', 'disp_id']
  success_url = '/computer'
  template_name = 'computer_form.html'

  def get_context_data(self, **kwargs):
    context = super(ComputerCreate, self).get_context_data(**kwargs)
    context['form'].fields['disp_id'] = forms.ModelChoiceField(queryset=DisplayClass.objects.all(), empty_label=None, label='Дисплейный класс')
    return context

class ComputerUpdate(UpdateView):
  model = Computer
  fields = ['cpu', 'graphic_card', 'disp_id']
  pk_url_kwarg = 'comp_id'
  success_url = '/computer'
  template_name = 'computer_form.html'

  def get_context_data(self, **kwargs):
    context = super(ComputerUpdate, self).get_context_data(**kwargs)
    context['form'].fields['disp_id'] = forms.ModelChoiceField(queryset=DisplayClass.objects.all(), empty_label=None, label='Дисплейный класс')
    return context

class ComputerDelete(DeleteView):
  model = Computer
  pk_url_kwarg = 'comp_id'
  success_url = '/computer'
  template_name = 'computer_delete_form.html'
