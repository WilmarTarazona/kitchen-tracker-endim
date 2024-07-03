# Kitchen Tracker
## Overview

The Kitchen Tracker is an advanced monitoring system that leverages YOLO (You Only Look Once) object detection framework to perform real-time pose detection of kitchen staff. This project is built using Python and connects to live cameras through RTSP (Real-Time Streaming Protocol) on a Local Area Network (LAN).

## Setup

To get started with the project, follow these steps:

1. Clone the repository and navigate to the project directory:

    ```shell
    git clone https://github.com/WilmarTarazona/kitchen-tracker-endim.git
    cd kitchen-tracker-endim
    ```

2. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Configuration

Before running the application, update the RTSP stream credentials to match your network's configuration. You can edit these settings directly in the configuration file or adjust them via the graphical user interface (GUI).

## Running the Application

To start the application, use the following command:

```shell
python main.py
```

## Development Phases

### Phase 1: Initial Development

During the initial phase, the focus is on implementing AI features to verify the accuracy and eligibility of pose estimation from various camera angles. This phase involves integrating the YOLO framework with the application to detect and analyze staff movements.

![Phase 1](images/Phase%201.jpg)

### Phase 2: GUI Development

In the second phase, a robust Python GUI is developed using PyQt. This GUI supports both dark and light themes and includes various components to enhance the functionality of the application, such as real-time video streaming, pose detection visualization, and configuration settings.

![Phase 2](images/Phase%202.jpg)

### Phase 3: Integration and Testing

The final phase involves integrating all previously developed components and conducting comprehensive testing to ensure seamless operation. This includes refining the GUI, optimizing the pose detection algorithm, and ensuring reliable connectivity with RTSP cameras.

![Phase 3](images/Phase%203.jpg)

## Features

- **Real-time Pose Detection:** Utilizes the YOLO object detection framework for accurate and real-time pose estimation.
- **RTSP Camera Integration:** Connects to live cameras using RTSP protocols on a LAN network for continuous monitoring.
- **User-Friendly GUI:** Features a PyQt-based graphical interface with support for dark and light themes.
- **Customizable Configuration:** Allows users to easily update LAN credentials and other settings via the GUI.
- **Comprehensive Monitoring:** Provides real-time visualization of staff movements and poses, enhancing kitchen safety and efficiency.
