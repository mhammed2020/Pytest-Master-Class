FROM ubuntu:20.04

# Install Nginx
RUN apt update 

# Create a directory 
RUN mkdir -p /tmp/scripts

# COPY
COPY magic.sh /tmp/scripts 

# Define workind directory 

WORKDIR /tmp/scripts

# Define default command 
 
CMD ["bash"]