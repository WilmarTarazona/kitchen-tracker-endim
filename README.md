# Kitchen Tracker

Staff pose detection using YOLO and Python, connecting to real-time cameras via RTSP protocols on a LAN network.

## Setup

First, clone the repository and navigate to the project directory:

```shell
git clone <repository-url>
cd kitchen-tracker-endim
```

## Install Dependencies

Install the required Python libraries:

```shell
pip install -r requirements.txt
```

## Run the Application

Before running the application, ensure to update your LAN credentials for RTSP protocol live streaming cameras. You can also change these settings via the GUI.

```shell
python main.py
```

## Development Phases

### Phase 1: Initial Development
Focus on AI features to verify the eligibility of pose estimation from various camera angles.

![Phase 1](images/Phase%201.jpg)

### Phase 2: GUI Development
Development of a Python GUI using PyQt, with both dark and light themes. Adding components for enhanced app functionality.

![Phase 2](images/Phase%202.jpg)

### Phase 3: Integration
Integrating the previous development stages into a cohesive application.

![Phase 3](images/Phase%203.jpg)

## Features

- Real-time pose detection using YOLO
- Connects to cameras via RTSP protocols on a LAN network
- User-friendly GUI with theme options
- Customizable LAN credentials
