# fast-flask

A flask starter template with postgreSQL database and deployed to Heroku.

## Getting Started (Development)

Clone the repository.

`git clone https://github.com/pikulet/fast-flask-example`
`cd fast-flask-example`

Install virtualenv.

`pip3 install virtualenv`

Activate the virtual environment.

`source venv\bin\activate`

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



