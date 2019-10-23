# coding:utf-8

from setuptools import setup, find_packages


packages = find_packages('typeidea')
print(packages)

setup(
    name='typeidea',
    version='0.1',
    description='blog',
    author='lvwenqi',
    author_email='769972594@qq.com',
    packages=packages,
    package_dir={'': 'typeidea'},
    include_package_data=True,
    install_requires=[
        'django==2.0.12',
    ],
    scripts=[
        'typeidea/manage.py',
    ],
)
