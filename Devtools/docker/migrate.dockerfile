FROM debian

WORKDIR /var/www/html/challenge/app
ENV APP=runner.py

RUN apt-get update
RUN apt-get install -y build-essential python3-dev python3-pip python3-setuptools python3-wheel 
RUN apt-get install -y python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 
RUN apt-get install -y libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
RUN apt-get install -y apache2 curl python3 python-mysqldb python3-mysqldb
RUN apt-get install -y default-libmysqlclient-dev python-dev  python-dev  libapache2-mod-wsgi-py3
COPY challenge /var/www/html/challenge
RUN pip3 install -r /var/www/html/challenge/requirements.txt 
RUN apt clean all
COPY docker/conf/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh