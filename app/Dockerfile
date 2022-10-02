FROM python:3.8-slim-buster AS Prod
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD [ "flask", "--app", "final", "run", "-h", "0.0.0.0", "-p", "8080" ]
