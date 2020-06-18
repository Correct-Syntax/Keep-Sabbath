from setuptools import setup


setup(
  name = 'keep_sabbath',   
  packages = ['keep_sabbath'],   
  version = '0.6.1',
  license='BSD 3-Clause',   
  description = 'Django app to automatically redirect users when it is the Sabbath day, with support for overriding on other Biblical Holy days.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = 'Correct Syntax, Noah Rahm', 
  author_email = 'correctsyntax@yahoo.com',     
  url = 'https://correctsyntax.com/projects/keep-sabbath/', 
  keywords = ['sabbath', 'django', 'web', 'redirects'], 
  install_requires=[           
          'django>=2.2'
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
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)

