FROM ubuntu:latest
LABEL authors="michael.brunner"

ENTRYPOINT ["top", "-b"]