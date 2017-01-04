from django.views.generic import TemplateView
from django.conf.urls import include, url, patterns
from django.contrib import admin

from example.demo import views as demo


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^live-update/$', view=demo.live_update, name='live_update'),
    url(r'^live-update-with-tokens/$', view=demo.live_update_with_token,
        name='live_update_with_token')
]

urlpatterns += patterns('',
    (r'^payu/', include('payu.urls')),
)
