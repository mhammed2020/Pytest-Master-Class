
FROM ubuntu:20.04 

# Install nginx
RUN \
    apt-get update &&\
    apt-get install -y net-tools &&\ 
    apt-get install -y iputils-ping &&\ 
    apt install -y curl && 

# Define working directory

WORKDIR /etc
# Define default command
CMD ["bash"]