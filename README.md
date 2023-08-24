# Django CRUD API 
The goal of this exercise is to retrieve data from an external source, store it in an appropriate database structure, and create a CRUD RESTful API to interface with the database. 

### Goals: 
1. **Read the data from this endpoint:** 

    [swapi-graphql.netlify.app/.netlify/functions/index?query=query Query %7BallPlanets%7Bplanets%7Bname population terrains climates%7D%7D%7D](https://swapi-graphql.netlify.app/.netlify/functions/index?query=query%20Query%20%7BallPlanets%7Bplanets%7Bname%20population%20terrains%20climates%7D%7D%7D)

    Additionally, you can view the shape of the data here: 

    [Explorer | Star Wars@current | Studio (apollographql.com)](https://studio.apollographql.com/public/star-wars-swapi/variant/current/explorer)

    with the following query: 

    query Query {allPlanets{planets{name population terrains climates}}}

2. **Store the data from the endpoint into the database and create appropriate models.**

3. **Write RESTful Create, Read, Update, and Delete endpoints to interact with the database.**

# Django REST API with Docker and Virtual Environment

This project demonstrates how to create a Django REST API using Docker for database hosting, a virtual environment for Python dependencies, and populating the database with data from a GraphQL API.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- Python (for managing dependencies within the virtual environment)
- `virtualenv` (if not already installed)

## Setup

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:Rafael13es/django-code-challenge-fwscience.git
   cd django-code-challenge-fwscience
   
2. **Create a Virtual Environment:**

    ```bash
    # Install virtualenv if not already installed
    pip install virtualenv

    # Create a virtual environment named 'venv'
    virtualenv venv

3. **Activate the Virtual Environment:**
    - On Windows:
        ```bash
        .\venv\Scripts\activate
    
    - On macOS and Linux:
        ```
        source venv/bin/activate
      
4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

5. **Docker Compose Setup:**
    ```bash
    # Build and start Docker containers
    docker-compose up -d

    # Apply database migrations
    docker-compose exec web python manage.py migrate

6. **Fetch Data from SWAPI GraphQL:**
    To populate your PostgreSQL database with data from the SWAPI GraphQL API, run the following Django management command:
    ```bash
    python manage.py populate_planets

## Running the Project

1. **Once everything is set up, you can run your Django project:**

    ```bash
    docker-compose up

The Django development server will start, and your API will be accessible at **http://localhost:8000/.**

## Contributing
Feel free to contribute to this project by opening issues or pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
