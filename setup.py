
import setuptools
from distutils.core import setup

setup(
  name = 'easytoken',         
  packages = ['easytoken'],   
  version = '1.0.1',      
  license='MIT', 
  long_description = 'easytoken is an independent Open Source, Natural Language Processing python library which implements a easytoken to create token from Both Sentence and Paragraph.',
  description = 'easytoken is an independent Open Source, Natural Language Processing python library which implements a easytoken to create token from Both Sentence and Paragraph.',  
  author = 'Sayan MOndal(ph3n1x)',               
  author_email = 'sayanmondal2098@gmail.com',     
  url = 'https://github.com/sayanmondal2098/easytoken',   
  download_url = 'https://github.com/sayanmondal2098/easytoken',   
  keywords = ['NLP', 'Natural Language Processing', 'Tokenization', 'Text Summarization', 'Text Processing', 'Sentiment Analysis'],   # Keywords that define your package best
  install_requires=[         
          'nltk',
          're',
          'sys',
          'os',
          'itertools',
          'string',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)