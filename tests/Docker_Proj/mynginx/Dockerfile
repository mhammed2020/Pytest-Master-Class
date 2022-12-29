FROM ubuntu:20.04 

RUN \
    apt update &&\
    apt install -y net-tools &&\ 
    apt install -y curl &&\ 
    apt install -y nginx &&\ 
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf &&\ 
    chown -R www-data:www-data /var/lib/nginx 

COPY index.html /var/www/html
COPY index2.html /var/www/html

WORKDIR /etc/nginx

CMD ["nginx"]

EXPOSE 80