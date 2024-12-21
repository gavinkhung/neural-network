FROM ubuntu:latest

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install packages as stated from https://github.com/HarisIqbal88/PlotNeuralNet
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra \
    git \
    poppler-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Python3 as default python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set working directory
WORKDIR /app
RUN git clone https://github.com/HarisIqbal88/PlotNeuralNet.git .

COPY . .

CMD cd architecture && bash ../tikzmake.sh nn; pdftoppm -png nn.pdf nn