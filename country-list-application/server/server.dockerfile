# Build documentation
FROM python:3.9 AS build-stage

WORKDIR /app/

# Install mkdocs
RUN python -m pip install --upgrade pip 
RUN pip install mkdocs mkdocs-material

COPY ./country-list-application/server /app/
COPY ./docs /app/

# Build the docs site
RUN mkdocs build
# RUN ls site && ./yeet

# Set up the server
FROM nginx:latest

WORKDIR /app
COPY --from=build-stage /app/site /usr/share/nginx/html/dev/docs
COPY --from=build-stage /app/nginx.conf /etc/nginx/conf.d/default.conf
