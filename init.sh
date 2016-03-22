#!/bin/sh
#sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
#sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
#sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
sudo service mysql restart
mysql -uroot -p << EOF
create user 'db_user'@'localhost' identified by 'qwery';
create database ask_db;
grant all on ask_db.* to 'db_user'@'localhost';
exit
EOF
python ask/manage.py syncdb
sudo python ask/manage.py runserver 0.0.0.0:80
