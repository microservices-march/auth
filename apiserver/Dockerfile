FROM nginx
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/
RUN mkdir /etc/nginx/njs
COPY ./njs/jwt.js /etc/nginx/njs/