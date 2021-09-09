FROM registry.redhat.io/ubi8/python-39
USER 0
COPY ./app /app
RUN chown -R 1000:0 /app 
USER 1000
RUN pip install -r /app/requirements.txt && \ 
python /app/model.py
EXPOSE 5000
CMD [ "python3", "-u", "/app/app.py" ]
