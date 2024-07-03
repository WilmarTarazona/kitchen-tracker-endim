# Kitchen Tracker
Staff pose detection using YOLO and Python, connecting to real time cameras via RTSP protocols on LAN network
## Setup
```shell script
git clone
cd kitchen-tracker-endim
```
## Install libraries
```shell script
pip install requirements.txt
```
## Run the app
> Note: Change LAN credentials to own for use of RTSP protocol livestreaming cameras or change via GUI
```shell script
python main.py
```
<table>
    <tr>
        <p>Initial phase of development focusing on AI features to verify eligibility of pose estimation from angles of the cameras</p>
        <img src="images/Phase 1.jpg" width="600"/>
    </tr>
    <tr>
        <p>Development of Python GUI using PyQt, implementing dark and light theme. Adding components for functionality of app</p>
        <img src="images/Phase 2.jpg" width="600"/>
    </tr>
    <tr>
        <p>Integration of previous development stages</p>
        <img src="images/Phase 3.jpg" width="600"/>
    </tr>
</table>