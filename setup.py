from setuptools import setup, find_packages

setup(
    name='django-airfields',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description="A Django app for managing airport and airfield data.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    author_email='sankarebarri@yahoo.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTP',
    ],
    install_requires=[
        'Django>=5.0',
    ]
)
