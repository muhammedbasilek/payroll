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

python -m venv myenv
myenv\Scripts\activate
cd payroll_frontent
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

steps to follow (linex/mac)-

python -m venv myenv
myenv\bin\activate
cd payroll_frontent
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
