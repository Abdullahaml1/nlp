# Instructions

## Build Docker Image
```bash
docker build -t nlpd .
```

## Run the image to prouce container
```bash
docker run -it --gpus all --name "name the container" -p 8888:8888 nlpd bash
```


## Run jupytar notebook
Install `jupyter lab`
```bash
pip install --upgrade jupyterlab
```
install vim-enabled jupyter using [jupyterlab-vim](https://github.com/jupyterlab-contrib/jupyterlab-vim)
```bash
pip install --upgrdae jupyterlab-vim
```
Run jupyterlab
```bash
jupyter lab --ip 0.0.0.0 --allow-root --no-browser
```

For old notebook run:
```bash
jupyter notebook --ip 0.0.0.0 --allow-root --no-browser
```



