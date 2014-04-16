fuga
====

Installation
=============
```
- git clone git@github.com:abbas123456/fuga.git
- cd fuga
- mkvirtualenv fuga
- pip install -r deploy/requirements.txt
- cd sites
- ./manage.py test
- ./manage.py syncdb
- ./manage.py migrate
- ./manage.py import_xml_file mobile_products/integration/example.xml 
- ./manage.py runserver
```
