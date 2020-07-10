<<<<<<< HEAD
# res_assignment

SQL Qureies
CREATE TABLE `BucketList`.`tbl_user` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_username` VARCHAR(45) NULL,
  `user_password` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));

```sql
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
# flask_app
>>>>>>> bc10c08feacdf6a2000ff3598953eb0b7ba73b61
