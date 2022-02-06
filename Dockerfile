FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
MAINTAINER TestAdmin


COPY ./requirements.txt /requirements.txt
RUN apt-get update \
	&& apt-get install libpq-dev gcc libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 ffmpeg libsm6 libxext6 -y \
	&& apt-get clean
RUN pip install -r /requirements.txt

RUN mkdir /wt
WORKDIR /wt
COPY ./wt /wt

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser testadmin
RUN chown -R testadmin /vol/
RUN chown -R testadmin /usr/local/lib/
RUN chown -R testadmin /wt/
RUN chmod -R 777 /vol/web/
USER testadmin