# Create user
CREATE USER 'myuser' IDENTIFIED BY 'mypassword';

# Create DB
CREATE DATABASE `mydb`;

# Grant ALL Access
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@% IDENTIFIED BY 'mypassword';

# Grant DB access
GRANT USAGE ON *.* TO 'myuser'@'%';
GRANT ALL PRIVILEGES ON `some-db`.* TO 'myuser'@% IDENTIFIED BY 'mypassword';

# Show Users
select * from user;

CREATE USER 'someapp'@'localhost' IDENTIFIED BY 'f22c2a6b00aacbcc423df17def845c2d27fd1c7aa5d5420af48a0a53e777b0b3';
GRANT ALL PRIVILEGES ON `someapp`.* TO 'someapp'@'localhost' IDENTIFIED BY 'f22c2a6b00aacbcc423df17def845c2d27fd1c7aa5d5420af48a0a53e777b0b3';
f22c2a6b00aacbcc423df17def845c2d27fd1c7aa5d5420af48a0a53e777b0b3

# Allow user all privileges on specific database
GRANT ALL PRIVILEGES ON lite.* TO 'vitor.esposito'@'%' WITH GRANT OPTION;

# Show grants
show grants for `israel.dias`@`%`;

# Create user with read access to DB_NAME:
CREATE USER '<username>' IDENTIFIED BY '<some-random-password>';
GRANT SELECT ON `DB_NAME`.* TO '<username>'@'%';
FLUSH PRIVILEGES;


# Update password
SET PASSWORD FOR 'someuser'@'%' = PASSWORD('somepassword');


# Drop user
DROP USER '<username>'@'%';


# create dump
mysqldump -h hostname -u username -p database_name -P port > file.sql

# Import dump
mysql -u username -h hostname -p < file.sql

## Debugging slow queries
```
SHOW PROCESSLIST; # Show you any queries that are currently running or in the queue to run
show status where `variable_name` = 'Threads_connected'; # Show all connected threads
show variables like 'max_connections'; # Show maximum number of allowed connections
```
