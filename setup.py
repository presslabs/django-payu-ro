# -*- encoding: utf-8 -*-
# Copyright 2012-2016 PressLabs SRL
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
Python setup file for the django-silver app.

In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:

    python setup.py register

If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:

    python setup.py sdist

Inspect the output thoroughly. There shouldn't be any temp files and if your
app includes staticfiles or templates, make sure that they appear in the list.
If something is wrong, you need to edit MANIFEST.in and run the command again.
If all looks good, you can make your first release:

    python setup.py sdist upload

For new releases, you need to bump the version number in
silver/__init__.py and re-run the above command.

For more information on creating source distributions, see
http://docs.python.org/2/distutils/sourcedist.html
"""

from setuptools import setup, find_packages

import payu

install_requires = [line.strip()
                    for line in open("requirements.txt").readlines()
                    if not line.strip().startswith('#') and line.strip()]

setup(
    name='django-payu-ro',
    version=payu.__version__,
    author='Presslabs SRL',
    author_email='support@presslabs.com',
    url='http://github.com/PressLabs/django-payu-ro',
    description='A pluggable Django application for integrating PayU Payments (ex. ePayment)',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
