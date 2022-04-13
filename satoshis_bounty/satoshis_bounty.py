from constructs import Construct
from .hitcounter import HitCounter
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from cdk_dynamo_table_view import TableViewer

class SatoshisBounty(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
            
        my_lambda = _lambda.Function(
            self, 'ApiController',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='controller.handler',
        )

        api_controller_with_counter = HitCounter(
            self, 'ApiControllerHitCounter',
            downstream=my_lambda,
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=api_controller_with_counter._handler,
        )

        TableViewer(
            self, 'ApiControllerViewHitCounter',
            title='API calls made',
            table=api_controller_with_counter.table,
            sort_by="-hits"
        )