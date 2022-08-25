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


# Installing nvim
RUN apt purge neovim -y
RUN apt update & apt upgrade -y
RUN add-apt-repository ppa:neovim-ppa/stable -y
RUN apt install neovim -y
# vimplug
RUN sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
RUN mkdir -p /root/.config/nvim
COPY init.vim /root/.config/nvim

#instalng Node and npm for coc (nvim autocompletion)
RUN cd /root && wget https://nodejs.org/dist/v16.17.0/node-v16.17.0-linux-x64.tar.xz && tar -xf node-v16.17.0-linux-x64.tar.xz
RUN echo $'# Node and npm  \n\
export PATH=/root/node-v16.17.0-linux-x64/bin${PATH:+:${PATH}}' >> /root/.bashrc
RUN pip3 install jedi


WORKDIR /root
