FROM debian:11-slim

ARG DEBIAN_FRONTEND=nointeractive

ARG USER_NAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN  apt update \
  && apt install -y -q \
     sudo \
     bash-completion \
     wget \
     curl \
     udev \
     usbutils \
     libusb-1.0-0 \
     libpython2.7 \
     python3 \
     python3-venv \
     git

## Set up udev rules for PlatformIO
RUN  wget -P /etc/udev/rules.d/ https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules \
  && service udev restart 

# Add user account and add to sudo group (password-free)
RUN  groupadd --gid $USER_GID $USER_NAME \
  && adduser --uid $USER_UID --gid $USER_GID --disabled-password --gecos "" $USER_NAME \
  && usermod -a -G dialout $USER_NAME \
  && usermod -a -G plugdev $USER_NAME \
  && echo "$USER_NAME ALL = NOPASSWD: ALL" > /etc/sudoers.d/user \
  && chmod 0440 /etc/sudoers.d/user

# Install PlatformIO CLI
USER $USER_NAME
RUN  wget -P /tmp https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py \
  && python3 /tmp/get-platformio.py \
  && /home/$USER_NAME/.platformio/penv/bin/pio system completion install bash \
  && echo 'export PATH="$PATH:$HOME/.platformio/penv/bin"' | tee -a /home/$USER_NAME/.bashrc \
  && echo 'export PATH="$PATH:$HOME/.platformio/penv/bin"' | sudo tee -a /root/.bashrc

#RUN $HOME/.platformio/penv/bin/pio pkg install --platform espressif32

CMD ["/bin/bash", "-c"]
