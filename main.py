import os

REGION = os.getenv('REGION', 'us-west-1')
ENV_NAME = os.getenv('ENV_NAME', 'PRODUCTION')

print(f"REGION: {REGION}")
print(f"ENV_NAME: {ENV_NAME}")
