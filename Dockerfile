FROM python:3.7-stretch

#RUN cat /etc/issue

COPY . /jsonplaceholder_tests
WORKDIR /jsonplaceholder_tests

RUN pip install -r requirements.txt

#ENTRYPOINT ["py.test", "--alluredir=reports","--testrail","--tr-config=testrail.cfg", "--verbose", "-k"]
ENTRYPOINT ["sleep"]
CMD ["99999"]