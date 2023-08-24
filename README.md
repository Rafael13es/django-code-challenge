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
   * On Windows:
        ```bash
        .\venv\Scripts\activate
    
   * On macOS and Linux:
        ```
        source venv/bin/activate
      
4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

5. **Docker Compose Setup:**
    ```bash
    # Build and start PostgreSQL Database container
    docker-compose up -d db

## Running the Project

1. **Once everything is set up, you can run your Django project:**

    ```bash
    # Build Django App container
    docker-compose build
   
    # Start Django App container
    docker-compose up

The Django development server will start, and your API will be accessible at **http://localhost:8000/.**.

## Usage

* Access Get all Planets and Create Planet endpoints: http://0.0.0.0:8000/api/planets/.
* Access Get a Planet by id, Update a Planet and Delete a planet endpoints: http://0.0.0.0:8000/api/planets/<int:pk>.

> [!NOTE]
> You can use this endpoints in the web browser for an interactive UI to gather the information.
> I created a [Postman Collection](django-crud.postman_collection.json) if you want a more traditional approach.

## Contributing
Feel free to contribute to this project by opening issues or pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
