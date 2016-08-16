FROM nginx:alpine
COPY ./dino /usr/share/nginx/html
EXPOSE 80


