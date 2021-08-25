#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

apt -y update
apt -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data
sed -i "/^\tserver_name/ a\\\n\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
service nginx restart
