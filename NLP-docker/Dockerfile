FROM tensorflow/tensorflow:latest-gpu 

RUN apt update && apt upgrade -y

RUN apt install git openssh-client openssh-server neovim  curl tree -y

# Installing python packages
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

RUN pip3 install notebook 
RUN pip3 install --user -U nltk
RUN pip3 install --user -U numpy
RUN python -m pip install scipy
RUN pip3 install matplotlib
RUN pip3 install transformers datasets 

