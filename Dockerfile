#This is the docker file for ctf pwn topic
from ubuntu:18.04
maintainer genesis
run apt-get update
run apt-get upgrade -y
run apt-get install -y libc6-i386 xinetd

