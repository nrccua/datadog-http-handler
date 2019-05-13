from setuptools import setup

setup(name='datadog-http-handler',
      version='1.0.0',
      description='Python logging module allowing you to log to directly to Datadog via https',
      url='https://github.com/nrccua/datadog-http-handler',
      author='Tim Reichard',
      author_email='tim.reichard@nrccua.org',
      license='MIT',
      packages=['datadog-http-handler'],
      install_requires=['requests'],
      zip_safe=False)