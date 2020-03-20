
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='django-session-header',
    version='1.0',
    description='Identify the Django Session by a Header',
    python_requires='==3.*,>=3.6.0',
    project_urls={"repository": "https://github.com/ryanhiebert/django-session-header"},
    author='Ryan Hiebert',
    author_email='ryan@ryanhiebert.com',
    license='MIT',
    packages=['django_session_header'],
    package_dir={"": "src"},
    package_data={},
    install_requires=['django==3.*,>=3.0.0'],
    extras_require={"dev": ["black==19.*,>=19.3.0", "codecov==2.*,>=2.0.0", "dephell==0.*,>=0.8.2", "pylint==2.*,>=2.3.0", "pytest==4.*,>=4.3.0", "pytest-cov==2.*,>=2.6.0", "pytest-django==3.*,>=3.4.0", "rope==0.*,>=0.14.0"], "drf": ["djangorestframework==3.*,>=3.9.0"]},
)
