FROM python:3.9-bullseye

# Set bash as shell
SHELL ["/bin/bash", "-c"]

# Create the deployment and other directories
RUN mkdir /workspace

# Environment variables
ENV PYTHONPATH="/workspace"

# Working directory
WORKDIR /workspace

# Update system and install required dependencies
RUN apt-get update && \
    apt-get -y upgrade

# Install Bazel
ARG BAZEL_VERSION=4.2.1

RUN apt-get install -y --no-install-recommends \
        apt-transport-https \
        curl \
        gnupg

RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > /etc/apt/trusted.gpg.d/bazel.gpg

RUN echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list

RUN apt-get update && \
    apt-get install -y --no-install-recommends bazel-$BAZEL_VERSION \
    openjdk-11-jdk && \
    ln -s /usr/bin/bazel-$BAZEL_VERSION /usr/bin/bazel && \
    bazel version

# Install Scala
RUN wget https://downloads.lightbend.com/scala/2.12.12/scala-2.12.12.deb && \
    dpkg -i scala-2.12.12.deb
