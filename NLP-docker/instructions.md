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
```bash
jupytar notebook --ip 0.0.0.0 --allow-root --no-browser
```



