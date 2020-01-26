# easytoken
[![Gitter](https://badges.gitter.im/BreadandCode/community.svg)](https://gitter.im/BreadandCode/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![CircleCI](https://circleci.com/gh/sayanmondal2098/easytoken.svg?style=svg)](https://circleci.com/gh/sayanmondal2098/easytoken)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/sayanmondal2098/easytoken/fork)
[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

 <p align="center">
  <img  src="https://bread-and-code.github.io/images/projects/easytoken.png">
</p>

# easytoken
easytoken is an independent Open Source, Natural Language Processing python library which implements a easytoken to create token from Both Sentence and Paragraph. It will also return the POS of the corresponding token .<br>
<br>

# Next in Line:
This is still in alpha stage so we are planning to add few more feature as  cleaning which will be added by 2020. We are also developing a other Language Processing algorithm for our library.

# Naming:
The name is just it's purpose \_(^_^)_/

# Installation and Implementation:
To install easytoken follow the steps:<br>
## Windows
Install pip:
```
$ python get-pip.py
```
Install via pip:
```
$ pip install easytoken
```
For upgrade:
```
$ pip install --upgrade easytoken
```
## Linux/Unix
Install pip:
```
$ python3 get-pip.py
```
Install via pip:
```
$ python3 -m pip install easytoken
```
For upgrade:
```
$ python3 -m pip install --upgrade easytoken
```
After Download the module ,:
```
$ python
>>> import nltk
>>> nltk.download("all")
```
Implementation:
```python
>>> from easytoken.easytoken import Wordeasytoken
>>> from easytoken.blob import Partsofspeech
>>>Wordeasytoken.tokenize(Wordeasytoken,text="Hello all , I'll be a good lover for you.")
>>> print   (Partsofspeech.pos("Hello all , I'll be in love with you."))
```
  
# Developer Info:
Author: Sayan Mondal<br>
Author-email: sayanmondal2098@gmail.com<br>
Team: Bread and Code

# Required Libraries:
          'nltk',
          're',
          'itertools',
          'os',
          'sys',
          'string'

# LISCENSE:
```
MIT License

Copyright (c) 2020 Sayan Mondal | Bread-and-Code

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

