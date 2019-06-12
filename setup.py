# -*- coding: utf-8 -*-
# @Time    : 2019-06-12 19:44
# @Author  : henson
# @Email   : henson_wu@foxmail.com
# @File    : setup.py.py
# @Software: PyCharm
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open("VERSION") as f:
    VERSION = f.read()

install_packages = []

setup(
    name='blog_server',
    version=VERSION,
    description=u'博客',
    long_description=readme,
    author='henson_wu',
    author_email='henson_wu@foxmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={
        "blog_server": ["*.jar"]
    },
    entry_points={
        'console_scripts': [
            'blog-server-starter=blog_server.wsgi:product'
        ]
    }
)
