# Django CRUD API 
The goal of this exercise is to retrieve data from an external source, store it in an appropriate database structure, and create a CRUD RESTful API to interface with the database. 

## Goals: 
## 1. Read the data from this endpoint: 

[swapi-graphql.netlify.app/.netlify/functions/index?query=query Query %7BallPlanets%7Bplanets%7Bname population terrains climates%7D%7D%7D](https://swapi-graphql.netlify.app/.netlify/functions/index?query=query%20Query%20%7BallPlanets%7Bplanets%7Bname%20population%20terrains%20climates%7D%7D%7D)

Additionally, you can view the shape of the data here: 

[Explorer | Star Wars@current | Studio (apollographql.com)](https://studio.apollographql.com/public/star-wars-swapi/variant/current/explorer)

with the following query: 

query Query {allPlanets{planets{name population terrains climates}}} 

## 2. Store the data from the endpoint into the database and create appropriate models.

## 3. Write RESTful Create, Read, Update, and Delete endpoints to interact with the database.
