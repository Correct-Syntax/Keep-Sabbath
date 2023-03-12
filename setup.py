from setuptools import setup


setup(
  name = 'keep_sabbath',   
  packages = [
    'keep_sabbath',
    'keep_sabbath.vendor',
  ],   
  version = '0.7.0',
  license='BSD 3-Clause',   
  description = 'Django app to automatically redirect users when it is the Sabbath day, with support for overriding on other Biblical Holy days.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = 'Noah Rahm', 
  author_email = 'hi@noahrahm.com',     
  url = 'https://github.com/Correct-Syntax/Keep-Sabbath/', 
  keywords = ['sabbath', 'django', 'web', 'redirects'], 
  install_requires=[           
    'django>=3.2'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: BSD License',   
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)

