import json
import os
from aliyunsdkcms.request.v20190101.DescribeMetricListRequest import DescribeMetricListRequest
from aliyunsdkcore.client import AcsClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials and configuration from environment variables
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
ACCESS_KEY_SECRET = os.getenv('ACCESS_KEY_SECRET')
REGION_ID = os.getenv('REGION_ID', 'ap-southeast-5')

# Client initialization for CMS
cms_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION_ID)

def get_metric_data(metric_name, namespace, dimensions, period='86400', start_time=None, end_time=None):
    try:
        request = DescribeMetricListRequest()
        request.set_MetricName(metric_name)
        request.set_Namespace(namespace)
        request.set_Period(period)
        request.set_StartTime(start_time)
        request.set_EndTime(end_time)
        request.set_Dimensions(dimensions)

        response = cms_client.do_action_with_exception(request)
        response = json.loads(response)

        return json.loads(response['Datapoints'])
    except Exception as e:
        print(f"Error retrieving metric data for {metric_name}: {e}")
        return []
