from aws_cdk import (
    aws_guardduty as gd,
    core
)
import json

class CdkGdMaster(core.Construct):

    @property
    def detectorId(self):
        return self._detector.ref

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)
        
        self._detector = gd.CfnDetector(
            self, 
            'Detector',
            enable=True,
            finding_publishing_frequency='FIFTEEN_MINUTES'
        )

        for account in kwargs['accounts']:

            construct_name = "memberinvitation" + account['Id'] 
            
            gd.CfnMember(
                self,
                construct_name,
                detector_id=self._detector.ref,
                email=account['Email'],
                member_id=account['Id'],
                disable_email_notification=True
            )
