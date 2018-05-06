from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class PatientListView(ListView):
    context_object_name = 'patients'
    model=models.Patient
    template_name = 'patient_list.html'

class PatientDetailView(DetailView):
    context_object_name = 'patient_detail'
    model=models.Patient
    template_name = 'patient_detail.html'

class PatientCreateView(CreateView):
    model = models.Patient
    fields=('fname','mname','lname','gender','dob')

class PatientUpdateView(UpdateView):
    fields = ('fname','mname','lname','gender','dob')
    model = models.Patient

class PatientDeleteView(DeleteView):
    model = models.Patient
    success_url = reverse_lazy('patient:list')