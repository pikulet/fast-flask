# fast-flask

A flask starter template with postgreSQL database and deployed to Heroku.

## Getting Started (Development)

Clone the repository.

`git clone https://github.com/pikulet/fast-flask-example`
`cd fast-flask-example`

Install virtualenv.

`pip3 install virtualenv`

Create a virtual environment.

`virtualenv venv`

Activate the virtual environment.

`source venv\bin\activate`

Install the python modules.

`pip3 install -r requirements.txt`

## Development

Start the database server.

`psql -U <username> -d <db_name>`

Run the app.

`flask run`

## Deployment to Heroku

Login to Heroku.

`heroku login`

Create Heroku app.

`heroku apps:create <heroku_app_name>`

Create a PostgreSQL database on Heroku. We use the free plan.

`heroku addons:add heroku-postgresql:hobby-dev`

Configure environment variables for Heroku.

`heroku config:set FLASK_APP=fastflask.py`

Push to Heroku remote.

`git push heroku master`



