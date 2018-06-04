#!/usr/bin/env python

from setuptools import setup


install_requires = [
    'sentry>=7.0.0',
    'requests'
]

setup(
    name='sentry-im',
    version='0.1.0',
    author='kolapapa',
    author_email='18740398549@163.com',
    url='https://github.com/kolapapa/sentry_im',
    description=__doc__,
    license='property',
    packages=['sentry_im'],
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'sentry_im=sentry_im',
        ],
        'sentry.plugins': [
            'sentry_im=sentry_im.plugin:IMPlugin'
        ],
    },
    classifiers=[
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent'
    ],
)
