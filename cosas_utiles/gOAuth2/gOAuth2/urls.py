from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('social_auth.urls')),
	url(r'^$', TemplateView.as_view(template_name="login.html")),
	url(r'^logout/$', logout, {'next_page': '/'}, name='gauth_logout'),
	url(r'^secrets/$', login_required(TemplateView.as_view(template_name="secrets.html"))),
    # Examples:
    # url(r'^$', 'gOAuth2.views.home', name='home'),
    # url(r'^gOAuth2/', include('gOAuth2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
