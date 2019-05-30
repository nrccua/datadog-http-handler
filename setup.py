'''Python logging module allowing you to log directly to Datadog via https.'''

from setuptools import setup

with open("README.md", "r") as handle:
    long_description = handle.read()

setup(name='datadog-http-handler',
      version='1.0.1',
      description='Python logging module allowing you to log directly to Datadog via https',
      long_description=long_description,
      url='https://github.com/nrccua/datadog-http-handler',
      author='NRCCUA Architects',
      author_email='architecture@nrccua.org',
      license='MIT',
      packages=['datadog_http_handler'],
      install_requires=['requests'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False,
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])
