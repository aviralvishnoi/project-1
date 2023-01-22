from aws_cdk import (
    Duration,
    Stack,
)
from utils.environment import MyEnv
from constructs import Construct
# from custom_constructs.s3 import S3Bucket, S3BucketProps
from custom_constructs.s3 import S3Bucket, S3BucketProps
from custom_constructs.iam_role import IamRole, IamRoleProps
from custom_constructs.lambda_function import LambdaFunction, LambdaProps
class Project1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        deploy_environment = MyEnv.DEV.value
        """
        1. Create s3 bucket for the application
        """
        bucket_name = "s3-" + self.node.try_get_context(deploy_environment)["app_name"] + "-" + self.node.try_get_context(deploy_environment)["team"] + "-" + deploy_environment 
        bucket_props = self.node.try_get_context(deploy_environment)["s3"]
        print(f"bucket_props = {bucket_props}")
        s3_bucket = S3Bucket(
            self,
            "AyodhyaBucket", S3BucketProps(
                bucket_name,
                # bucket_props
            )
        )

        """
        2. Create IAM role for s3 bucket
        """
        role_name = "iam-role-" + self.node.try_get_context(deploy_environment)["app_name"] + "-" + self.node.try_get_context(deploy_environment)["team"] + "-" + deploy_environment
        lambda_role = IamRole(
            self,
            "AyodhyaRole", IamRoleProps(
                role_name,
                s3_bucket.get_bucket_arn
            )
        )
        """
        3. Create lambda function
        """
        # lambda_iam_role=iam_role.get_lambda_role_arn
        # print(lambda_iam_role)
        print(f"{lambda_role.get_lambda_role_name}")
        lambda_name="lambda-" + self.node.try_get_context(deploy_environment)["app_name"] + "-" + self.node.try_get_context(deploy_environment)["team"] + "-" + deploy_environment

        lambda_function=LambdaFunction(
            self,
            "AyodhyaLambdaFunction1",
            LambdaProps(
                lambda_name,
                lambda_role.get_lambda_role_arn
            )
        )

