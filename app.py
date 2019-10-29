#!/usr/bin/env python3

from aws_cdk import core
from cdk_guardduty.guardduty_master_stack import CdkGdMaster

class MyStack(core.Stack):
    def __init__(self, scope: core.App, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        resource = CdkGdMaster(
            self, 'GdMaster',
            accounts=[{'Id':'12312312312', 'Email':'test@test.test'},
                      {'Id':'34534534512', 'Email':'sop@test.test'},
                      {'Id':'12312222212', 'Email':'teeee@test.teset'}]
        )

app = core.App()
MyStack(app, "cdk-guardduty")
app.synth()
