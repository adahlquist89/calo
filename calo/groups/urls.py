from django.conf.urls import patterns, include, url
from groups.models import Group
from django.views.generic import ListView, DetailView

urlpatterns = patterns('',
	url(r'^$', ListView.as_view(queryset=Group.objects.all(), allow_empty=True, template_name='index.html')),
	#grupo especifico con detail view o hacer una class based view que herede de DetailView si queremos agregar alguna que otra funcionalidad
	)