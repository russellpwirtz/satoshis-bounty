#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_workshop_python.cdk_workshop_python_stack import CdkWorkshopPythonStack


app = cdk.App()
CdkWorkshopPythonStack(app, "cdk-workshop-python")

app.synth()
