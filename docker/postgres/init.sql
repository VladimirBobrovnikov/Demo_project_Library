CREATE user vova WITH PASSWORD '123456';

CREATE DATABASE users_db;
GRANT ALL PRIVILEGES ON DATABASE users_db TO vova;
CREATE DATABASE books_db;
GRANT ALL PRIVILEGES ON DATABASE books_db TO vova;
CREATE DATABASE issues_db;
GRANT ALL PRIVILEGES ON DATABASE issues_db TO vova;
