# Copyright (c) 2017 Presslabs SRL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.views.generic import TemplateView
from django.conf.urls import include, re_path
from django.contrib import admin

from example.demo import views as demo


urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name="home.html")),
    re_path(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    re_path(r'^live-update/$', view=demo.live_update, name='live_update'),
    re_path(r'^obtain-ipn-token/$', view=demo.obtain_ipn_token,
        name='obtain_ipn_token'),
    re_path(r'^alu-payments/', view=demo.ALUPayments.as_view(),
        name='alu_payments'),
    re_path(r'^token-payments/', view=demo.TokenPayments.as_view(),
        name='token_payments'),
    re_path(r'^debug/', view=demo.debug,
        name='debug')
]

urlpatterns += [
    re_path(r'^payu/', include('payu.urls')),
]
