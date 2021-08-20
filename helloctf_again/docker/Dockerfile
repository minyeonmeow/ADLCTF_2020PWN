#from ctf
from ubuntu:latest
maintainer genesis

RUN apt-get update -y
RUN apt-get install -y xinetd
run useradd -m helloctf
cmd ["/usr/sbin/xinetd", "-dontfork"]
