FROM nginx

WORKDIR /app

COPY ./nginx.conf /etc/nginx/conf.d/default.conf