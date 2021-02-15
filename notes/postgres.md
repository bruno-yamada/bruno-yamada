# Postgres Cheatsheet

## Login
psql -h <host> -U
psql -h <host> -U -d <database>

# List Databases
\l

# List Tables
\dt
> details
\dt+

# Export data
\copy (SELECT * FROM persons) to '/tmp/persons_client.csv' with csv

# Describe table
SELECT table_name, column_name, data_type FROM information_schema.columns WHERE table_name = 'fgt';

# List Users (and Roles)
\du

# List databases
\l

# Connect do Database
\c <db_name>

# Disconnect from Database
\q

# Create user

CREATE USER username WITH PASSWORD 'password';

# Grant
## Connect
GRANT CONNECT ON DATABASE database_name TO username;
## Usage
GRANT USAGE ON SCHEMA schema_name TO username;
## SELECT
### Grant SELECT for a specific table:
GRANT SELECT ON table_name TO username;
### Grant SELECT for multiple tables:
GRANT SELECT ON ALL TABLES IN SCHEMA schema_name TO username;

### If you want to grant access to the new table in the future automatically, you have to alter default:
ALTER DEFAULT PRIVILEGES IN SCHEMA schema_name
GRANT SELECT ON TABLES TO username;

# Show tables grants
select * from information_schema.table_privileges where grantee = 'car_tag_billing_service_read';

# Add search path to user
ALTER ROLE username SET search_path SET database;

# Expanded mode
\x on
\x off

# List schemas
\dn+

# Drop user
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM car_tag_billing_service_read;
REVOKE ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public FROM car_tag_billing_service_read;
REVOKE ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public FROM car_tag_billing_service_read;
REVOKE ALL PRIVILEGES ON DATABASE car_tag_billing_service FROM car_tag_billing_service_read;
DROP USER car_tag_billing_service_read;

# set search path in this session
SHOW search_path
SET search_path to <path>, public, ...

# list privileges
\z car_tag_billing_service

---

# Refs:
https://marcyes.com/2016/0922-messing-with-postgresql-users-and-permissions/
> privileges
https://www.postgresql.org/docs/12/ddl-priv.html

# Create readonly user through role
## With postgres user
CREATE ROLE role_name;
CREATE USER username LOGIN PASSWORD somepassword;
GRANT role_name to username;
## with schema owner if exists
\c database
GRANT usage ON SCHEMA schema_name TO role_name;
GRANT select ON ALL TABLES IN SCHEMA schema_name TO role_name;
GRANT select ON ALL SEQUENCES IN SCHEMA schema_name TO role_name;
REVOKE truncate ON ALL TABLES IN SCHEMA schema_name FROM role_name;
> Talvez não precise do abaixo:
ALTER DEFAULT PRIVILEGES FOR USER username IN SCHEMA schema_name GRANT select ON TABLES TO role_name;
ALTER DEFAULT PRIVILEGES FOR USER username IN SCHEMA schema_name REVOKE truncate ON TABLES FROM role_name;
ALTER DEFAULT PRIVILEGES FOR USER username IN SCHEMA schema_name GRANT select ON SEQUENCES TO role_name;

##### TODO convert
Padrão de grant:

Logar na base postgres com o user postgres:
1 - CREATE USER data_pipeline WITH PASSWORD 'xyz';

Ainda logado com o user postgres, acessar a base do serviço (ex: overflow_manager_service)
2 - GRANT USAGE ON SCHEMA overflow_manager_service to data_pipeline;

Logar na base do serviço com o user do serviço (ex: overflow_manager_service)
3 - GRANT USAGE ON SCHEMA overflow_manager_service to data_pipeline;
4 - GRANT SELECT ON ALL TABLES IN SCHEMA overflow_manager_service to data_pipeline;
5 - GRANT SELECT ON ALL SEQUENCES IN SCHEMA overflow_manager_service to data_pipeline;

# Slow running queries
SELECT pid, client_addr, backend_start, query FROM pg_stat_activity ORDER BY backend_start;

