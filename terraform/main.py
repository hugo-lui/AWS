from constructs import Construct
from cdktf import App, NamedRemoteWorkspace, TerraformStack, TerraformOutput, RemoteBackend
from imports.aws.provider import AwsProvider
from imports.aws.instance import Instance


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="us-west-1")

        instance = Instance(self, "compute", ami="ami-01456a894f71116f2", instance_type="t2.micro")

        TerraformOutput(self, "public_ip", value=instance.public_ip)


app = App()
stack = MyStack(app, "aws_instance")

RemoteBackend(stack, hostname='app.terraform.io', organization='icedm0chi', workspaces=NamedRemoteWorkspace('AWS'))

app.synth()
