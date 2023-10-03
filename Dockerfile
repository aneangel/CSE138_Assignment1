FROM Python:3.11
COPY . /Assignment1.py
RUN make /Assigment1.py
CMD python /Assignment1.py