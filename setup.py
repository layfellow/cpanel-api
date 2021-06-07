from setuptools import setup

setup(
    name = 'cpanel-api',
    version = '0.3.1',
    url = "https://github.com/tz4678/cpanel-api",
    author = "Sergey M",
    author_email = "tz4678@gmail.com",
    description = "CPanel API Client. Supports cPanel API 2 and UAPI.",
    packages = ['cpanel_api'],
    install_requires = ['requests>=2.24.0,<3.0', 'pysocks>=1.7.1,<2.0'],
    python_requires = '>=3.8'
)
