-- The order of dropping (existing) tables matters, to prevent referential integrity issues.
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),  -- FK (foreign key) to users table.
  description VARCHAR(255),
  duration INT,
  completed BOOLEAN
);