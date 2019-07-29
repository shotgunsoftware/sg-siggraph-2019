FROM python:2-alpine

RUN apk add --no-cache git

COPY requirement.txt ./
RUN pip install -r requirement.txt

COPY ./src /shotgun_events/src

WORKDIR /shotgun_events/src

VOLUME /shotgun_events/plugins
VOLUME /shotgun_events/logs

ENTRYPOINT [ "./shotgunEventDaemon.py" ]
CMD [ "foreground" ]