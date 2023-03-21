CREATE TABLE netflix (
    show_id VARCHAR(255) PRIMARY KEY,
    type VARCHAR(255),
    title VARCHAR(255),
    director VARCHAR(255),
    actors VARCHAR(1000),
    country VARCHAR(255),
    date_added TIMESTAMP,
    release_year INT,
    rating VARCHAR(255),
    duration VARCHAR(255),
    listed_in VARCHAR(255),
    description TEXT
);

CREATE TABLE disney (
    show_id VARCHAR(255) PRIMARY KEY,
    type VARCHAR(255),
    title VARCHAR(255),
    director VARCHAR(255),
    actors VARCHAR(1000),
    country VARCHAR(255),
    date_added TIMESTAMP,
    release_year INT,
    rating VARCHAR(255),
    duration VARCHAR(255),
    listed_in VARCHAR(255),
    description TEXT
);