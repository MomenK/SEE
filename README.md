# SEE
Software for data visulaization 
# requirments 
### Xampp
### Python
### MySQL
### Django
  
# Steps:
1. Install Python 2.7 with pip
2. Add python to the environment variables
3. install XAMPP - need PHP and MySQL to be be able to use phpmyadmin
4. install Django and dependancies
  ```Bash
  pip install Django
  pip install django_extensions
  pip install djangorestframework
  ```
 Make sure to install mysql version 1.3.4, other version need Python3

```Bash
  pip install mysqlclient==1.3.4
```
5. install numpy and pySerial
```Bash
  pip install numpy
  pip install pyserial
```
6. import database template (found in db folder) to "test" table using phpmyadmin.
6a. (Optional) rest primary key "id" to one
```sql
ALTER TABLE [tablename] AUTO_INCREMENT = 1
```
or through phpmyadmin operation tab

7. fake intial database migrations
```Bash
  python manage.py  migrate --fake-initial
```
8. run test code in the project directory 
```Bash
  python populate.py
```