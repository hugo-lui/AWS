import boto3

ec2 = boto3.client("ec2")

instancesResponse = ec2.describe_instances()
print(instancesResponse)

ec2Response = ec2.run_instances(
    ImageId = "ami-022661f8a4a1b91cf",
    InstanceType = "t2.micro",
    MaxCount = 1,
    MinCount = 1,
)

print(ec2Response)