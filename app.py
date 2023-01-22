import os

import aws_cdk as cdk

from project_1.project_1_stack import Project1Stack
from utils.environment import MyEnv

app = cdk.App()
Project1Stack(app, "Project1Stack",
    synthesizer=cdk.DefaultStackSynthesizer(
        # synthesizer properties
        file_assets_bucket_name="cdk-aviral-bootstrap"
    )
    )

app.synth()
