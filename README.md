# newyearservice

Print how many days are left until the new year

To build docker image: sudo docker build -t service https://github.com/alekszalata/newyearservice.git

To run: sudo docker run -i --rm -p 8000:8000 service

possible addresses:

http://127.0.0.1:8000/daystillNY/ 

http://127.0.0.1:8000/daystillNY/Value/

Instead Value you can put other years
