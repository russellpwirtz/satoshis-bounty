#!/usr/bin/env python3

import aws_cdk as cdk

from satoshis_bounty.satoshis_bounty import SatoshisBounty

app = cdk.App()
SatoshisBounty(app, "satoshis-bounty-python")

app.synth()
