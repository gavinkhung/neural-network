ARG REGISTRY=quay.io
ARG OWNER=jupyter
ARG BASE_IMAGE=$REGISTRY/$OWNER/scipy-notebook
FROM $BASE_IMAGE

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /home/jovyan/work

# Install PyTorch with pip (https://pytorch.org/get-started/locally/)
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --index-url 'https://download.pytorch.org/whl/cpu' \
    'torch' \
    'torchaudio' \
    'torchvision' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Install the Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the JupyterLab port
EXPOSE 8888

RUN mkdir -p vanishing_gradients

# Start the JupyterLab server
CMD ["start.sh", "jupyter", "lab", "--NotebookApp.token=''"]