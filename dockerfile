FROM httpd:latest
COPY index.html /usr/local/apache2/htdocs/
COPY style.css /usr/local/apache2/htdocs
COPY script.js /usr/local/apache2/htdocs/