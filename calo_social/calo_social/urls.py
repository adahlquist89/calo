from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^friends/", include("calo_social.friends.urls")),

    
    url(
        r"^account/social/connections/$",
        TemplateView.as_view(template_name="account/connections.html"),
        name="account_social_connections"
    ),
    url(r"^account/social/", include("social_auth.urls")),
    # url(
    #     r"^account/login/$",
    #     TemplateView.as_view(template_name="account/signup.html"),
    #     name="account_login"
    # ),
    # si dejo el de abajo, no me carga bien el form del sign up
    # url(
    #     r"^account/signup/$",
    #     TemplateView.as_view(template_name="account/signup.html"),
    #     name="account_signup"
    # ),
    url(r"^account/", include("account.urls")),
    url(r"^account/signup/$",
        TemplateView.as_view(template_name="account/signup_auth.html"),
        name="auth_signup"
    ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
