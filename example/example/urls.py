from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += patterns('',
    (r'^payu/', include('payu.urls')),
)

urlpatterns += patterns('example.demo.views',
    (r'^$', 'home'),
)
