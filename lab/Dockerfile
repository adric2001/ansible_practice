FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Install SSH server, python, sudo, curl, system tools
RUN apt-get update && apt-get install -y \
    openssh-server \
    python3 \
    python3-apt \
    python3-pip \
    sudo \
    curl \
    iproute2 \
    procps \
    vim \
    systemd-sysv \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Setup SSH directory
RUN mkdir -p /var/run/sshd /root/.ssh && chmod 700 /root/.ssh

# Create ansible test user with passwordless sudo
RUN useradd -m -s /bin/bash ansible && \
    echo "ansible:ansible" | chpasswd && \
    echo "ansible ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ansible && \
    chmod 0440 /etc/sudoers.d/ansible && \
    mkdir -p /home/ansible/.ssh && \
    chmod 700 /home/ansible/.ssh && \
    chown -R ansible:ansible /home/ansible/.ssh

# Configure SSH daemon
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
