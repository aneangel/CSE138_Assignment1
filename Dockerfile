# I used Cheng-Wei Dockerfile that he provided for the class to help wrtie this file
# found here: https://canvas.ucsc.edu/courses/64879/files/7803437?module_item_id=1128322 as well as, Docker resources
# found here: https://www.docker.com/blog/how-to-dockerize-your-python-applications/

FROM python:3

ADD Assignment1.py /

#RUN pip3 install json \
#    pip3 install urlib.parse


CMD ["python",  "./Assignment1.py", "-p 8090"]