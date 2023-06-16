FROM registry.redhat.io/ubi8/python-39
USER 0
WORKDIR /app
COPY . /app
RUN chown -R 1000:0 /app
USER 1000
RUN pip install --upgrade pip && \
pip --no-cache-dir install -r requirements.txt && \ 
python model.py
EXPOSE 5000
CMD [ "python3", "-u", "app.py" ]
