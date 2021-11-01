# About

This simple API consists of a single endpoint where we can send a country code and see the 
list of countries. To solve the problem of finding a path from one country to another, I represent the 
map of countries as an undirected, acyclic graph with the vertices being the countries
connected by an edge if they are adjacent to each other. The backend will then find 
the shortest path between two countries by finding the shortest path between the countries
in the graph using [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).
Although this may be overkill for this small of a project, this can easily be expanded to 
Graphs with hundreds of thousands of vertices to find the shortest path. 

The backend is written in [Python](https://www.python.org/) and deployed
using [Docker](https://www.docker.com/) and [Nginx](https://www.nginx.com/) on an Ubuntu server
hosted by [Digital Ocean](https://www.digitalocean.com/). The project comes complete with automated
unit testing, static type analysis, linting and formatting, and continuous integration. 
See the sections below for an elaboration on each part of the project.


## Structure

The backend for this project is written in [Python](https://www.python.org/) using the 
[FastAPI](https://fastapi.tiangolo.com/) framework. All of the backend code lies in
the `country-list-application/backend` directory. The primary endpoint is defined in 
the `backend/app/app/api` directory as Python `async` function attached to a route.
All of the routes are collected and initialized in the `backend/app/app/main.py` file,
which is run using the [uvicorn](https://www.uvicorn.org/) library. 

The logic for the shortest path algorithm to find the path between two countries 
lies in the `backend/app/app/graph` directory. It relies on the 
[NetworkX](https://networkx.org/) Python library to form the country graph
and to find the shortest path using Dijkstra's Algorithm. This `graph`
module exposes a function that the primary route uses to find the shortest path. 

Basic config and settings for the backend can be found in the 
`backend/app/app/config/settings.py` file. Any global settings and fundamental configuration 
details are placed in this file and imported throughout the project.

## Deployment

The backend API is built inside of a [Docker](https://www.docker.com/) container. I use
[Nginx](https://www.nginx.com/) to serve the backend in another Docker container. To 
coordinate the server container and the backend container easily, I use Docker Compose.
Both the Nginx server and Backend containers are hosted on a [Digital Ocean](https://www.digitalocean.com/)
at [countrylist.brodenwanner.com](https://countrylist.brodenwanner.com).

## Testing

Automated backend unit tests are written using [pytest](https://docs.pytest.org/en/6.2.x/) and 
can be found in the `backend/app/app/tests` directory. To run the unit tests, simply navigate
to the `backend/app` directory and run the command `pytest` in the terminal. Also note that the
unit tests are run on every push to the remote repository and the results of the unit tests
can be examined there.

[Codecov](https://about.codecov.io/) generates reports about how much of the codebase was 
executed for the unit tests. Codecov integrates with GitHub, and a Codecov report is generated
on every push to the remote repository. The `pytest-cov` plugin is used to generate these
reports.

## Documentation

Documentation is written in MarkDown and compiled together into a website using 
[MkDocs](https://www.mkdocs.org/) and the Material theme. 

API docs are automatically generated by FastAPI and can be found at
[countrylist.brodenwanner.com/redoc](https://countrylist.brodenwanner.com/redoc).

## Future Work

Given a graph $G = (V, E)$ where $V$ is the vertex set and $E$ is the edge set, Dijkstra's 
Algorithm runs in $O(|V| + |E|)$ time. This works for smaller graphs, but solving this problem
for graphs with millions of vertices can be intractable. At that point, it may be 
more advantageous to use a heuristic search algorithm such as [A*](https://en.wikipedia.org/wiki/A*_search_algorithm).

Furthermore, as the number of vertices expands, a graph database will have to be used
since it would be impossible to store the entire graph in memory. 
