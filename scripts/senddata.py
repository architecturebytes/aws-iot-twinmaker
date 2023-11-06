import boto3
import datetime
import random
import time
 
# AWS SiteWise Alias
alias = '/factory/Motor1/Speed'
 
# Create a Boto3 SiteWise client (Make sure region_name is the one you plan to use)
client = boto3.client('iotsitewise', region_name='us-east-1')
 
# Send data at 1-second intervals indefinitely
while True:
    speed = round(random.uniform(100, 1000), 2)  # Generate a random speed value between 100 and 1000
    epoch = int(time.time())  # Get the current epoch timestamp using time.time()
 
    # Create the JSON payload
    payload = {
        "entries": [
            {
                "entryId": str(epoch),
                "propertyAlias": alias,
                "propertyValues": [
                    {
                        "value": {
                            "doubleValue": speed
                        },
                        "timestamp": {
                            "timeInSeconds": epoch
                        },
                        "quality": "GOOD"
                    }
                ]
            }
        ]
    }
 
    # Send the data to AWS SiteWise
    try:
        response = client.batch_put_asset_property_value(entries=payload['entries'])
        print("Data sent successfully: {}".format(payload))
    except Exception as e:
        print("Error sending data: {}".format(e))
 
    time.sleep(1)  # Wait for 1 second before sending
