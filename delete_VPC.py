# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def delete_vpc(vpc_id):
    
    try:
        response = vpc_client.delete_vpc(VpcId=vpc_id)

    except ClientError:
        logger.exception('This Could not delete the vpc.')
        raise
    else:
        return response


if __name__ == '__main__':
    VPC_ID = input("Please enter the VPC ID")
    vpc = delete_vpc(VPC_ID)
    logger.info(f'Wow, Your VPC {VPC_ID} is deleted successfully.')