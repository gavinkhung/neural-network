# Neural Network

Neural Network Implementation using Gradient Descent algorithm, Linear Algebra, NumPy, and Matplotlib. The corresponding PyTorch code is also implemented.

## Usage

### Running the program

```bash
jupyter notebook
```

### Running via Docker

Build the JupyterLab Docker image and start it

```bash
docker build -t neural-network .
docker run --rm -p 8888:8888 -v "$(pwd)":/home/jovyan/work neural-network
```

Open JupyterLab at the following URL: [http://127.0.0.1:8888/lab](http://127.0.0.1:8888/lab)

### Running via Docker Compose

Start the Docker image

```bash
docker compose up --build -d
```

Open JupyterLab at the following URL: [http://127.0.0.1:8888/lab](http://127.0.0.1:8888/lab)

Clean up the Docker container

```bash
docker compose down --volumes --rmi local
```

## Program Output

Numpy Implementation
![Neural Network without ML Library](./neural_network.gif "Neural Network Graphs Numpy")

Pytorch Implementation
![Neural Network with PyTorch](./neural_network_pytorch.gif "Neural Network Graphs PyTorch")
