FROM python:3

ADD Assignment1.py /

#RUN pip3 install json \
#    pip3 install urlib.parse


CMD ["python",  "./Assignment1.py", "-p 8090"]