# payroll
H &amp; R Test

Instructions on how to build/run your application:

-------------Frondend-----------------

required-

node : v18.17.1
npm: 9.6.7

steps to follow-

1) cd payroll_frontent
2) npm i
3) npm start

-------------Backend------------------

required-

python: 3.7

steps to follow (linex/mac)-

1) python -m venv myenv
2) myenv\bin\activate
3) pip install -r requirements.txt
4) python manage.py makemigrations
5) python manage.py migrate
6) python manage.py runserver

steps to follow (windows)-

1) python -m venv myenv
2) cd venv
3) source bin/activate
4) cd payroll_frontent
5) pip install -r requirements.txt
6) python manage.py makemigrations
7) python manage.py migrate
8) python manage.py runserver

*****************************************************************************************


How did you test that your implementation was correct?

Tested manually by changing the csv file data with different scenarios

*****************************************************************************************

If this application was destined for a production environment, what would you add or change?

Now the urls in the frontend are hardcoded,
Backend need to set da database like Postgressql, now it runs in sqlite3
Additional UI needed in frontend

*****************************************************************************************

What compromises did you have to make as a result of the time constraints of this challenge?

I took this challenge and completed in 5 hr, I most focused in backend development to make sure the API and the db design is more accurate

