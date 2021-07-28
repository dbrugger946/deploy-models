FROM fedora:33
RUN dnf -y update && dnf -y install python3 && dnf -y install python3-pip && dnf clean all
ADD ./app/requirements.txt /app/
RUN python3 -m pip install -r /app/requirements.txt
USER 1000
COPY ./app /app
EXPOSE 5000
CMD [ "python3", "-u", "/app/app.py" ]
