-- Create user and database

DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE  rolname = 'postgres') THEN

      CREATE ROLE my_user LOGIN PASSWORD 'postgres';
   END IF;
END
$do$;

SELECT 'CREATE DATABASE postgres'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'postgres')\gexec
GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;


-- Create tables

CREATE TABLE IF NOT EXISTS todos (
  id SERIAL PRIMARY KEY,
  text VARCHAR(255),
  completed BOOLEAN DEFAULT FALSE
);


-- Insert data

INSERT INTO todos (text)
VALUES ('Complete test assignment');
INSERT INTO todos (text)
VALUES ('Check new jobs');
INSERT INTO todos (text)
VALUES ('Buy a present');
INSERT INTO todos (text)
VALUES ('Go to the shop');