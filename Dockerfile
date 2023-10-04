FROM Python:3

ADD Assignment1.py /

RUN pip3 install socket \
    pip3 install json \
    pip3 install urlib.parse

CMD ["python",  "Assignment1.py"]