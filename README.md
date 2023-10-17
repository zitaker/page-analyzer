### Hexlet tests and linter status:
[![Actions Status](https://github.com/zitaker/python-project-83/workflows/hexlet-check/badge.svg)](https://github.com/zitaker/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/1871fbf00e66f9f7fca4/maintainability)](https://codeclimate.com/github/zitaker/python-project-83/maintainability)

#  Page Analyzer

[Demo](https://page-analyzer-of-the-georgia.onrender.com/)  

#### A page analyzer is an application that analyzes certain pages for their SEO suitability.  
The Page Analyzer is a full — fledged application based on the Flask platform, using PostgreSQL. The principle of building the MVC architecture is taken: working with routing, query handlers and templating, interacting with the database. Deployment takes place on render.com .  

### Opportunities
1. Entering a url and saving it in the urls table.
2. If you make a check, the data is stored in the url_checks table and connected by a foreign key by id to the urls table.
3. Output of data from two tables.
4. Output of messages when performing checks:
   * Page added successfully.
   * The page already exists.
   * Invalid URL.
   * The URL contains more than 255 characters.
   * An error occurred during verification.
   * The page has been successfully verified.


![Screenshot from 2023-10-16 19-39-32](https://github.com/zitaker/python-project-83/assets/92075508/37411b12-5ab7-4904-b837-2f640104adaa)

![Screenshot from 2023-10-16 19-38-07](https://github.com/zitaker/python-project-83/assets/92075508/21888cc6-d94f-42c4-b15f-3def148f27fa)

![Screenshot from 2023-10-16 19-38-46](https://github.com/zitaker/python-project-83/assets/92075508/6f7f8cc2-0899-4ec6-a3c8-1fd2c2f6eb48)

#### Minimum requirements:  
1. Python.
2. Pip.
3. Poetry.
4. Flask.
5. Gunicorn.
6. Python-dotenv.
7. Psycopg2-binary.
8. Pytest-cov.
9. Beautifulsoup4.
10. Werkzeug.
11. The database. I use is postgresql.

#### Install:
1. Download the project.
2. Go to the root directory of the project.
3. Log in to the virtual environment poetry by the command ```poetry shell```
4. Install the required packages with the command ```make loading```
5. Run the command to create tables ```make build```
