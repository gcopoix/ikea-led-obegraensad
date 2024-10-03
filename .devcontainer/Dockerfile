FROM node:18-bullseye-slim

ARG DEBIAN_FRONTEND=nointeractive

RUN  apt update \
  && apt install -y -q \
     sudo \
     bash-completion \
     wget \
     curl \
     udev \
     nano \
     usbutils \
     libusb-1.0-0 \
     libpython2.7 \
     python3 \
     python3-venv \
     git

# Set up udev rules for PlatformIO
RUN  wget -P /etc/udev/rules.d/ https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules \
  && service udev restart

# Add node user to plugdev, dialout and sudo group (password-free)
RUN  usermod -a -G dialout node \
  && usermod -a -G plugdev node \
  && echo "node ALL = NOPASSWD: ALL" > /etc/sudoers.d/user \
  && chmod 0440 /etc/sudoers.d/user

# Download and install JLink tools
RUN curl -d 'accept_license_agreement=accepted' \
     -X POST https://www.segger.com/downloads/jlink/JLink_Linux_x86_64.deb \
     -o /tmp/JLink_Linux_x86_64.deb \
  && dpkg --unpack /tmp/JLink_Linux_x86_64.deb \
  && rm /tmp/JLink_Linux_x86_64.deb \
  && rm -f /var/lib/dpkg/info/jlink.postinst \
  && (dpkg --configure jlink || apt install -yf) \
  && apt install -y libxrandr2 libxfixes3 libxcursor1

# Install PlatformIO CLI
USER node
RUN  wget -P /tmp https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py \
  && python3 /tmp/get-platformio.py \
  && $HOME/.platformio/penv/bin/pio system completion install bash \
  && echo 'export PATH="$PATH:$HOME/.platformio/penv/bin"' | tee -a /$HOME/.bashrc \
  && echo 'export PATH="$PATH:$HOME/.platformio/penv/bin"' | sudo tee -a /root/.bashrc

# globally install framework and toolings (needs to be installed only once in the docker)
RUN  $HOME/.platformio/penv/bin/pio pkg install --global --platform espressif32@6.9.0 \
  && $HOME/.platformio/penv/bin/pio pkg install --global --tool     framework-arduinoespressif32@3.20017.0 \
  && $HOME/.platformio/penv/bin/pio pkg install --global --tool     espressif/toolchain-riscv32-esp@8.4.0+2021r2-patch5 \
  && $HOME/.platformio/penv/bin/pio pkg install --global --tool     espressif/toolchain-xtensa-esp32@12.2.0+20230208 \
  && $HOME/.platformio/penv/bin/pio pkg install --global --tool     espressif/toolchain-xtensa-esp32s2@8.4.0+2021r2-patch5 \
  && $HOME/.platformio/penv/bin/pio pkg install --global --tool     tool-scons@4.40801.0 \
  && $HOME/.platformio/penv/bin/pio pkg install --global --tool     tool-mkspiffs@1.200.0 \
  && $HOME/.platformio/penv/bin/pio pkg install --global --tool     tool-mklittlefs@1.203.210628 \
  && $HOME/.platformio/penv/bin/pio pkg install --global --tool     tool-mkfatfs@2.0.1 \
  && $HOME/.platformio/penv/bin/pio system prune --cache --force

# Turn off git advice about detachedHead
RUN git config --global advice.detachedHead false

CMD ["/bin/bash", "-c"]
