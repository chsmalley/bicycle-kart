ARG VARIANT="jammy"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# Install linux packages
COPY .devcontainer/linux-packages.txt /tmp/tmp-pkgs/
RUN apt update && export DEBIAN_FRONTEND=noninteractive \
    && apt -y --no-install-recommends install $(cat /tmp/tmp-pkgs/linux-packages.txt | tr '\n' ' ') \
    && rm -rf /tmp/tmp-pkgs

# Install python packages
COPY .devcontainer/requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Not sure if this is necessary
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install

# COPY ./src/install $INST_SCRIPTS
# RUN bash $INST_SCRIPTS/install_retroarch.sh  && rm -rf $INST_SCRIPTS/

# tz
ENV TZ="America/New_York"
RUN localedef -i en_US -f UTF-8 en_US.UTF-8

# zsh plugins
USER vscode
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# copy rc file -> this will source as well
COPY .devcontainer/.zshrc /home/vscode/.zshrc

# workdir
WORKDIR /workspaces/tss4-trailer-adas-func-specs
CMD ["zsh"]