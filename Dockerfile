# I used Cheng-Wei Dockerfile that he provided for the class to help wrtie this file
# found here: https://canvas.ucsc.edu/courses/64879/files/7803437?module_item_id=1128322 as well as, Docker resources
# found here: https://www.docker.com/blog/how-to-dockerize-your-python-applications/

FROM python:3
RUN pip install flask

ADD Assignment1.py /

CMD [ "python3", "./Assignment1.py", "-p 8090" ]
