FROM tensorflow/tensorflow:latest-gpu 

RUN apt update #&& apt upgrade -y

RUN apt install git openssh-client openssh-server curl tree -y

# Installing python packages
RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

RUN pip install notebook 
RUN pip install --user -U nltk
RUN pip install --user -U numpy
RUN python -m pip install scipy
RUN pip install matplotlib
RUN pip install transformers datasets 
RUN pip install seaborn
RUN pip install jupyterlab
RUN pip install pandas
RUN pip install --upgrade tensorflow-hub
RUN pip install --upgrade tensorflow-datasets
RUN pip install jupyterlab-vim


# Installing nvim
RUN apt update #& apt upgrade -y
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
RUN pip install jedi

# Confuguring ssh

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config



WORKDIR /root
