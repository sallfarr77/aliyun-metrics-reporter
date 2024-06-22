import json
import os
from alibabacloud_ecs20140526.client import Client as EcsClient
from alibabacloud_ecs20140526.models import DescribeInstancesRequest
from alibabacloud_tea_openapi import models as open_api_models
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials and configuration from environment variables
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ACCESS_KEY_SECRET')
REGION_ID = os.getenv('REGION_ID', 'ap-southeast-5')
ENDPOINT = os.getenv('ENDPOINT', 'ecs.ap-southeast-5.aliyuncs.com')

# Ensure credentials are available
if not ACCESS_KEY_ID or not ACCESS_KEY_SECRET:
    raise ValueError("ACCESS_KEY_ID and ACCESS_KEY_SECRET must be set in the .env file")

# Client initialization for ECS
ecs_config = open_api_models.Config(
    access_key_id=ACCESS_KEY_ID,
    access_key_secret=ACCESS_KEY_SECRET,
    region_id=REGION_ID,
    endpoint=ENDPOINT
)
ecs_client = EcsClient(ecs_config)

def get_instance_name(instance_id):
    """Retrieve the name of an ECS instance by its ID."""
    try:
        request = DescribeInstancesRequest(
            instance_ids=json.dumps([instance_id]),
            region_id=REGION_ID
        )
        response = ecs_client.describe_instances(request)
        instances = response.body.instances.instance
        if instances:
            return instances[0].instance_name
        else:
            return "Unknown"
    except Exception as e:
        print(f"Error retrieving instance name for {instance_id}: {e}")
        return "Unknown"
