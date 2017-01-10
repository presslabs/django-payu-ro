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

import logging

from django.db.models import Q
from django.core.management.base import BaseCommand

from payu.models import PayUIDN

logger = logging.getLogger(__name__)


def string_to_list(list_as_string):
    return list(map(int, list_as_string.strip('[] ').split(',')))


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument(
            '--idns',
            help='A list of idns pks to be sent.',
            action='store', dest='idns', type=string_to_list
        )

    def handle(self, *args, **options):
        idns = PayUIDN.objects.filter(Q(sent=False) | Q(sent=True, success=False))

        if options['idns']:
            idns = idns.filter(pk__in=options['idns'])

        for idn in idns:
            idn.send()

            if not idn.success:
                logger.error('Encountered exception while processing idn'
                             'with id=%s, ex=%s.', idn.id, idn.response,
                             exc_info=True)
