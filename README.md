[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

# Flask_APP

App is structured in below manner

```
python-microservices/
.
├── flas_app/
│   ├── app/
│   │   ├── templates/
│   │   │   ├── addwish.html
│   │   │   ├── index.html
│   │   │   ├── signup.html
│   │   │   ├── error.html
│   │   │   ├── signin.html
│   │   │   ├── userhome.html
│   │   ├── static/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   ├── config.py
│   │   ├── requirements.txt
│   ├── db/
│   │   ├── init.sql
│   └── docker-compose.yml
│   └── Readme.MD
```

# To run this program 
1. Download and install docker and docker-compose
2. Clone the repo
2. Application uses MYSQL password from environment variables, please create .env file containing secrets in app/ directory
```
git clone 
cd flask_app/app
cat .env
SECRET_KEY='yoursecretkey'
MYSQL_DATABASE_USER='Username'
MYSQL_DATABASE_PASSWORD='password'
MYSQL_DATABASE_DB='DatabaseName'
MYSQL_DATABASE_HOST='HostName/ServiceName'
```
Create ur environment varibles. Go to flask_app and run below command
```
docker-compose up -d --build
```

# Problems
1. Broken SQL queries were used which prevented creating any table
2. Ajax button links missing - Becase of missing ajax button link, nothing happens when u click on signup
3. Response printed on console
4. Broken packages were imported
5. Broken code - wherever user Id is required whole user object was passed
6. Broken authentication - plain text was stored in db and which is then compared with hashed string resulting in mismatch
```
SQL Qureies
CREATE TABLE `BucketList`.`tbl_user` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_username` VARCHAR(45) NULL,
  `user_password` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));

sql
CREATE TABLE `BucketList`.`tbl_user` (
  `user_id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NOT NULL,
  `user_username` VARCHAR(45) NOT NULL,
  `user_password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`));
```
  Ajax button links were missing
```javascript
    <script src="../static/js/jquery-3.2.1.js"></script>
    <script src="../static/js/SignUp.js"></script>
```
 Then finally, go to the webpage click on the big sign up button, fill in some details and click "Sign up", nothing will happen, just so you know. Right click on 
the page somewhere and choose "Inspect Element" which should pop up a box along the bottom of the screen, choose the console, then on my browser Firefox, a few more 
options come up, click on "Logging" this is where you will see the fruits of your work. I hope that has been helpful to someone as it was driving me nuts!
 
 from flaskext.mysql import MySQL
 
=======
##Microservice architecture - repository structure
```
python-microservices/
.
├── user_service/
│   ├── usermanagement_service/
│   │   ├── api/
│   │   │   ├── usermanagement.py
│   │   │   ├── db_manager.py
│   │   │   ├── db.py
│   │   │   ├── models.py
│   │   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── wish_service/
...
```
