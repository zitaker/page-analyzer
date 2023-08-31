--DROP TABLE IF EXISTS url_checks;
--DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name varchar(255) NOT NULL,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);


--INSERT INTO urls (name) VALUES ('Arya');



SELECT * FROM urls;