# By MuZakkir Saifi
# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the REGION")

# this is the configration for the logger_for

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_responce = boto3.client("ec2", region_name=REGION)


def delete(vpc_id):
    
    try:
        res = vpc_responce.delete_vpc(VpcId=vpc_id)

    except ClientError:
        logger_for.exception('Oops sorry, Your VPC can not be deleted.')
        raise
    else:
        return res


if __name__ == '__main__':
    ID = input("Please enter the VPC ID")
    vpc = delete(ID)
    logger_for.info(f'Wow, Your VPC {ID} is deleted successfully.')