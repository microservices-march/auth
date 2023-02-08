FROM nginxplus
RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/conf
COPY secret.jwk /etc/nginx/conf/
COPY index.html /usr/share/nginx/html/