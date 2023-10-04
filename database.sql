--DROP TABLE IF EXISTS url_checks;
--DROP TABLE IF EXISTS urls;


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
--    created_at DATE NOT NULL DEFAULT CURRENT_TIMESTAMP
--    created_qwerty TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    created_at TIME DEFAULT CURRENT_TIMESTAMP
);

--CREATE TABLE urls (id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, name varchar(255) unique NOT NULL, created_at DATE NOT NULL DEFAULT CURRENT_TIMESTAMP);
--CREATE TABLE url_checks (id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, url_id bigint REFERENCES urls (id), status_code numeric, h1 text, title text, description text, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
--
--select u.id, u.name, uc.created_at from urls u join url_checks uc on u.id=uc.url_id;
--SELECT * FROM urls join created_qwerty from url_checks ORDER BY id DESC;

--INSERT INTO urls (name) VALUES ('Arya');
--INSERT INTO urls (name) VALUES ('Bron');

--INSERT INTO url_checks (h1) VALUES ('qwerty');
--INSERT INTO url_checks (url_id) VALUES (2);

SELECT * FROM urls;
SELECT * FROM url_checks;

--SELECT (urls.id, urls.name, url_checks.created_at) FROM urls FULL JOIN url_checks ON urls.id = url_checks.url_id ORDER BY urls.id DESC;

SELECT urls.id, urls.name, url_checks.created_at FROM urls FULL JOIN url_checks ON urls.id = url_checks.url_id ORDER BY urls.id DESC;

SELECT * FROM url_checks WHERE url_id = '1' ORDER BY created_at DESC LIMIT 1;


