# payroll
H &amp; R Test

-------------Frondend-----------------

required-

node : v18.17.1
npm: 9.6.7

steps to follow-

cd payroll_frontent
npm i
npm start

-------------Backend------------------

required-

python: 3.7

steps to follow (windows)-

1) python -m venv myenv
2) myenv\Scripts\activate
3) cd payroll_frontent
4) pip install -r requirements.txt
5) python manage.py makemigrations
6) python manage.py migrate
7) python manage.py runserver

steps to follow (linex/mac)-

1) python -m venv myenv
2) myenv\bin\activate
3) pip install -r requirements.txt
4) python manage.py makemigrations
5) python manage.py migrate
6) python manage.py runserver
