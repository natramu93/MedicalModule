from django.conf.urls import url
from patient import views

app_name='patient'

urlpatterns=[
    url(r'^$',views.PatientListView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$',views.PatientDetailView.as_view(),name='detail'),
    url(r'^create/$',views.PatientCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.PatientUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.PatientDeleteView.as_view(),name='delete'),
]