USE myapp;

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL
);

INSERT INTO messages (message) VALUES 
('Hello from the database!'),
('Welcome to our microservices app!'),
('Have a great day!');