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

import sys

import django
from django.conf import settings


settings.configure(
    DEBUG=True,
    ROOT_URLCONF="payu.urls",
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    PAYU_CALLBACK_URL="https://test.com",
    PAYU_LU_URL="https://test.com",
    PAYU_ALU_URL="https://test.com",
    PAYU_IDN_URL="https://test.com",
    PAYU_MERCHANT="PAYUDEMO",
    PAYU_KEY="1231234567890123",
    INSTALLED_APPS=(
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.admin",
        "payu",
    ),
    SECRET_KEY="dummy",
)


django.setup()
