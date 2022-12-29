# base image : alpine is used for its small size 
FROM alpine   

# packages  or depencies 

# RUN apk add --update redis 

# command to run on image 
CMD [ "echo","Hello from docker version 2 " ]
