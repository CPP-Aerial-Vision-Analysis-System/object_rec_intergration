FROM osrf/ros:noetic-desktop

# Add ubuntu user with the same UID and GID as the host system, if it doesn't already exist
ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN if ! id -u $USER_UID >/dev/null 2>&1; then \
        groupadd --gid $USER_GID $USERNAME && \
        useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME; \
    fi

# Add sudo support for the non-root user
RUN apt-get update && \
    apt-get install -y sudo && \
    echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# Switch from root to user
USER $USERNAME

# Add user to video group to allow access to webcam
RUN sudo usermod --append --groups video $USERNAME

# Update all packages
RUN sudo apt update && sudo apt upgrade -y

# Install Git
RUN sudo apt install -y git

# Rosdep update
RUN rosdep update

# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

# Install dependencies for cv_bridge and OpenCV
RUN sudo apt install -y ros-noetic-cv-bridge python3-opencv

# Install additional packages for OpenCV development
RUN sudo apt install -y libopencv-dev

# Setup for X11 host display permissions
# Allows GUI applications to access the host display
RUN sudo apt install -y x11-apps
ENV DISPLAY=:0
RUN sudo apt install -y xauth
RUN touch ~/.Xauthority

# Set environment variable to use X11 from the host machine (host.docker.internal)
RUN echo "export DISPLAY=\$(cat /etc/resolv.conf | grep nameserver | awk '{print \$2}'):0.0" >> ~/.bashrc
RUN echo "export QT_X11_NO_MITSHM=1" >> ~/.bashrc

# Reload bashrc to apply changes
RUN /bin/bash -c "source ~/.bashrc"

################################
## ADD ANY CUSTOM SETUP BELOW ##
################################
