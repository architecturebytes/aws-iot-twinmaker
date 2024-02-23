# AWS IoT TwinMaker Tutorial

**Refer YouTube video**: <br>
https://www.youtube.com/watch?v=P7cEi6oZTeM 

**scripts/senddata.py** <br>
Sends (motor) data to SiteWise <br>
Before, you run this script, make sure that your command line environment is setup for AWS access. <br>

**models/motor.glb** <br>
3D Motor model file

**CORS configuration for Grafana scene viewer** <br>
You need to configure CORS (cross-origin resource sharing) for the TwinMaker S3 bucket.<br>
Without this you may see this error in Grafana Scene Viewer: "Load 3D Scene failed with Network Failure" <br> 
Follow the CORS configuration steps here: https://docs.aws.amazon.com/iot-twinmaker/latest/guide/cors-configuration-grafana.html 
