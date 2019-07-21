# https://hub.docker.com/_/ubuntu/
FROM ubuntu:18.04

USER root

# Set password for root user
RUN echo "root:vukvukvuk" | chpasswd

# noninteractive basically means no GUI will be used
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -yq dist-upgrade && \
    apt-get install -yq --no-install-recommends \
    wget \
    curl \
    npm \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    nano \
    vim \
    htop && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Install Tini: https://github.com/krallin/tini
ENV TINI_VERSION v0.18.0
RUN wget --quiet --no-check-certificate https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini && \
    mv tini /usr/local/bin/tini && \
    chmod +x /usr/local/bin/tini

ENV CONDA_DIR=/opt/conda \
    SHELL=/bin/bash \
    USER=vukglisovic \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV PATH=$CONDA_DIR/bin:$PATH \
    HOME=/home/$USER

ENV MINICONDA_VERSION=latest
RUN mkdir -p $CONDA_DIR && \
    cd /tmp && \
    wget https://repo.continuum.io/miniconda/Miniconda2-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    /bin/bash Miniconda2-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda2-${MINICONDA_VERSION}-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \
    $CONDA_DIR/bin/conda config --system --set auto_update_conda false && \
    $CONDA_DIR/bin/conda config --system --set show_channel_urls true && \
    $CONDA_DIR/bin/conda update --all --yes && \
    $CONDA_DIR/bin/conda clean -tipsy && \
    rm -rf $HOME/.cache/yarn

RUN conda create -n swagger --yes \
    'python=3.6' \
    'flask'

RUN /bin/bash -c ". activate swagger && \
    pip install flask-restplus"

# app is running on port 5000
EXPOSE 5000
WORKDIR $HOME

# Configure container startup
ENTRYPOINT ["tini", "--"]
# When the docker is started up, the flask app is started up: https://github.com/moby/moby/issues/21650
ENV FLASK_APP app.py
CMD ["/opt/conda/envs/swagger/bin/python", "-m", "flask", "run", "--host=0.0.0.0"]

# Add local files as late as possible to avoid cache busting
COPY app.py shopping.py $HOME/
