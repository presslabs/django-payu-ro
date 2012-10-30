from setuptools import setup, find_packages

import payu

setup(
    name='django-payu',
    version=".".join(map(str, payu.__version__)),
    author='Calin Don',
    author_email='calin@presslabs.com',
    url='http://github.com/PressLabs/django-payu',
    install_requires=[
        'Django>=1.4'
    ],
    description = 'A pluggable Django application for integrating PayU Payments (ex. ePayment)',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)