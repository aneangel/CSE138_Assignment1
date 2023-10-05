# CSE138_Assignment1
Github repo for CSE138 Assignment 1

## Acknowledgments and Citations

--------------------------------

I used Cheng-Wei Dockerfile that he provided for the class to help write this file
found here: [canvas](https://canvas.ucsc.edu/courses/64879/files/7803437?module_item_id=1128322) as well as, 
Docker resources found here: [docker](https://www.docker.com/blog/how-to-dockerize-your-python-applications/)
I used Stackoverflow for inspiration on this portion to help understand how I could separate and differentiate between 
msg params and unwanted params found here: 
[Stackoverflow](https://stackoverflow.com/questions/12572362/how-to-get-a-string-after-a-specific-substring)
as well as docs.python for additional information on how to use urlparse found here: 
[python docs](https://docs.python.org/3/library/urllib.parse.html)

- I did not consult with any other students about this project for help (unless the TA counts then I did consult with a 
student for the project: his work per above)
 
-----------------------------------

#### Contents

- Assignment1.py: An HTTP web service that differentiates between requests with different HTTP verbs (GET
and POST) and URI paths (/hello, /hello/<name>, and /test).
- Dockerfile: Docker file to build container image of assignment 1
- Readme.md: Explanation of citations and file contents for assignment 1