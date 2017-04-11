FROM python
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -v -r requirements.txt
COPY . /usr/src/app
ENV FLASK_APP serve.py
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5042"]
EXPOSE 5042
