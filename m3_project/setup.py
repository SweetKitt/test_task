from setuptools import setup, find_packages

setup(
    name='m3_project',
    version='1.0.0',
    description='My project',
    author='Ekaterina',
    author_email='Faite@bk.ru',
    url='https://github.com/SweetKitt/test_task',
    packages=find_packages(),
    install_requires=[
        # список зависимостей
        'django==2.2.2',
        'm3-django-compat==1.9.2',
        'm3-objectpack==2.2.47',
    ],
)
