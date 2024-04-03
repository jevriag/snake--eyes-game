## Snake Eyes game app

This app is a dice rolling game for users to try to guess the outcome of a dice roll.
Users will be able:
- To Sign in/Register/Reset their credentials 
- To purchase a virtual currency with real money through Stripe
- Be able to subscribe by paying a few dollar per month
- To change their subscription plan 
- To track their invoice info

## Core tech Stack

- Flask
- Celery 
- Redis
- Stripe
- Sql Alchemy - Postgresql
- Click cli 
- Docker 

For the full list of dependencies see `package.json`
For the full list of dependencies see `requirements.py`

## How to run

The first thing to do is to clone the repository

    https://github.com/JevaG/Snake-eyes-app.git

Switch to the project directory and run
    
    docker-compose up --build

The application should now be accessible via `localhost:3000`
