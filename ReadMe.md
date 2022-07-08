# Link Shortener

The aim of this project is to convert the given links into shorter links and to direct the requests from the new links to the relevant links.
### Features
- Generating a 10 character link extension for the given link.
- Keeping the number of requests for shortened links.
- Redirecting requests from shortened links to original links.

### Structure 
- It was created with the Microservice structure.
- Django framework is used on Python.
- Relational database is used as database.
- Message queue structure is used for data consistency and inter-service communication.

### Setup
- There are two django projects as web and admin.
- Link management (link adding, listing and number of incoming requests) is done with admin.
- Requests for shortened links on the web are managed.
- For installation, the database information to be used is entered in the DATABASES section of the two projects. The necessary link is entered in the MQ_URL part of the queue structure.
- I used rabbitmq on cloudamqp with a postgresql database on digitalocean while running it myself.
- In addition, it is expected that docker will be installed on the system used.
- After all the requirements are provided, the following commands are run within the two projects, and the projects are runned.

```sh
cd admin
docker-compose build
docker-compose up
```

```sh
cd web
docker-compose build
docker-compose up
```
### Usage
- Link Building - POST -> 0.0.0.0:8000/link/ 
body -> {
    "main_link":"https://www.blabla.com"
}
- Listing links - GET -> 0.0.0.0:8000/link/
- Link redirecting - GET -> http://0.0.0.0:8001/shortening
