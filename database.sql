DROP TABLE IF EXISTS url_checks;
DROP TABLE IF EXISTS urls;


CREATE TABLE urls (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name varchar(255) unique NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE url_checks (
    id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    url_id bigint REFERENCES urls (id),
    status_code numeric,
    h1 text,
    title text,
    description text,
    created_at DATE NOT NULL DEFAULT CURRENT_TIMESTAMP
);



--INSERT INTO urls (name) VALUES ('Arya');
--INSERT INTO urls (name) VALUES ('Bron');

--INSERT INTO url_checks (h1) VALUES ('qwerty');
--INSERT INTO url_checks (url_id) VALUES (2);

SELECT * FROM urls;
SELECT * FROM url_checks;
