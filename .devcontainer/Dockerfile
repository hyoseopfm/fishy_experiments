################################################################################
# Base
#  - a single-version python debian image
# Installs
#  - development tools
#  - adds a user called 'zen'
# Size
#  - 300MB
################################################################################

ARG PYTHON_VERSION=3.8.15
ARG UBUNTU_VERSION=

FROM ubuntu:${UBUNTU_VERSION}

ARG NAME=python-zen

################################################################################
# Development Tools
################################################################################

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    graphviz \
    make \
    bash \
    bash-completion \
    ca-certificates \
    git \
    less \
    python3-dev \
    python3-pip \
    ssh \
    sudo \
    vim \
    wget

# GL Debs
RUN apt-get install -y --no-install-recommends \
    mesa-utils \
    libvulkan1 \
    libvulkan-dev \
    vulkan-tools \
    libegl1 \
    libgles2

# X11 Debs
#RUN apt-get install -y --no-install-recommends \
#    libasound2-dev
#RUN apt-get install -y --no-install-recommends \
#    libudev-dev
#RUN apt-get install -y --no-install-recommends \
#    libx11-dev
#RUN apt-get update
#RUN apt-get install -y --no-install-recommends \
#    x11-apps
#RUN apt-get install -y --no-install-recommends \
#    x11-xserver-utils
#RUN apt-get install -y --no-install-recommends \
#    libxkbcommon-dev
#RUN apt-get install -y --no-install-recommends \
#    libxkbcommon-x11-0

RUN apt-get update && apt-get install -y --no-install-recommends \
    libasound2-dev \
    alsa-utils \
    libudev-dev \
    libx11-dev \
    x11-apps \
    x11-xserver-utils \
    libxkbcommon-dev \
    libxkbcommon-x11-0

RUN apt-get autoremove \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

################################################################################
# Python Tools
################################################################################

RUN pip install --upgrade pip \
    && \
    pip install ursina[extras]

ARG UV_VERSION=0.5.15
ARG UV_HOME=/opt/uv
ARG PYRIGHT_VERSION=1.1.391
ARG RUFF_VERSION=0.8.6

ENV UV_VERSION=${UV_VERSION}
ENV UV_HOME=${UV_HOME}
ENV PATH="${UV_HOME}/bin:$PATH"

RUN export UV_INSTALL_DIR="${UV_HOME}/bin" && curl --proto '=https' --tlsv1.2 -LsSf https://github.com/astral-sh/uv/releases/download/0.5.5/uv-installer.sh | sh && \
    echo "export PATH=${UV_HOME}/bin:\${PATH}" >> /etc/profile

RUN export UV_TOOL_BIN_DIR="${UV_HOME}/bin"  \
    && export UV_TOOL_DIR="${UV_HOME}/tools" \
    && uv tool install pyright@${PYRIGHT_VERSION} \
    && uv tool install ruff@${RUFF_VERSION}

################################################################################
# NVIDIA
################################################################################

ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics,display,video,utility,compute

################################################################################
# Login Shells for Debugging & Development
################################################################################

# In a login shell (below), the PATH env doesn't survive, configure it at ground zero
ENV TERM xterm-256color
ENTRYPOINT ["/bin/bash", "--login", "-i"]

################################################################################
# Development with a user, e.g. for vscode devcontainers
################################################################################

ARG USERNAME=zen
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN groupadd --gid $USER_GID $USERNAME
RUN useradd --uid $USER_UID --gid $USER_GID -s "/bin/bash" -m $USERNAME
RUN echo "${USERNAME} ALL=NOPASSWD: ALL" > /etc/sudoers.d/${USERNAME} && \
    chmod 0440 /etc/sudoers.d/${USERNAME}
RUN echo "export PS1='\[\033[01;36m\](docker)\[\033[00m\] \[\033[01;32m\]\u@${NAME}\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /home/${USERNAME}/.bashrc && \
    echo "alias ll='ls --color=auto -alFNh'" >> /home/${USERNAME}/.bashrc && \
    echo "alias ls='ls --color=auto -Nh'" >> /home/${USERNAME}/.bashrc

#    touch /home/${USERNAME}/.bash_completion && chown ${USERNAME}:${USERNAME} /home/${USERNAME}/.bash_completion

################################################################################
# Debugging with root
################################################################################

RUN echo "export PS1='\[\033[01;36m\](docker)\[\033[00m\] \[\033[01;32m\]\u@${NAME}\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ${HOME}/.bashrc && \
    echo "alias ll='ls --color=auto -alFNh'" >> ${HOME}/.bashrc && \
    echo "alias ls='ls --color=auto -Nh'" >> ${HOME}/.bashrc