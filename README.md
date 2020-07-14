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
1. Broken SQL queries were used which prevented creating any table, unique constraints, parameter sizes etc.
2. Ajax button links missing - Becase of missing ajax button link, nothing happens when u click on signup
3. Response printed on console
4. Broken packages were imported
5. Broken code - wherever user Id is required whole user object was passed
6. Broken authentication - plain text was stored in db and which is then compared with hashed string resulting in mismatch
7. MySQL running with root account
# Approach to containerize 
1. Configure the application locally solved all the issues and made it working
2. Split the applicationa and mysql db 
3. Created flask_app container - Issue occured /it was not exposed since default flask_app listens to loopback inside container
4. exposed the app with host=0.0.0.0
5. Created docker container for mysql  -Manually ran the script and checked whether everything is working fine
6. created boostrap script to initiate all the tables and stored procedures
7. Created a docker-compose file to link flask_app and mysqldb containers
8. Created github actions for source code review
# What can be done further
1. Use nginx proxy with uWSgi and split the app in views and APIs and data calls ```User - > Nginx --> uWsgi-view.py -> REST api.py -> Data_layer -> DB container```
2. Implement vault to store/use secrets
3. Implement API gateway to have communication among microservice layers (jwt flow)
4. Use db connection from non root user
5. Implement DevOps pipeline to build docker images from source code repository
6. Implement security unit test
7. Docker image scanning and container run time checks integration
8. Deployment in k8s/managed k8s

```+Firewall+ -> Front end-> Makes Request to backend APIs with (User Token)-> BFF(Backend For Frontend) --> Makes call to internal microserivce with APP token```

``Front end -> **API Gateway*** Backend For Frontend -> **API Gateway** Microservices```

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

## Microservice architecture - repository structure
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
