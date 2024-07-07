from aws_cdk import (
  aws_lambda as _lambda,
  aws_sqs as sqs,
  aws_sns as sns,
  aws_sns_subscriptions as subscriptions,
  aws_lambda_event_sources as lambda_event_sources,
  Stack,
)

from constructs import Construct

class CatalogBatchProcess(Stack):

  def __init__(self, scope: Construct, construct_id: str, environment, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    create_product_topic = sns.Topic(
      self, 'CreateProductTopic', topic_name='createProductTopic'
    )

    create_product_topic.add_subscription(subscriptions.EmailSubscription('kitelolga@int.pl'))

    catalog_items_queue = sqs.Queue(self, "CatalogItemsQueue", queue_name="catalogItemsQueue")

    event_source = lambda_event_sources.SqsEventSource(catalog_items_queue, batch_size=5)

    environment['SNS_TOPIC_ARN'] = create_product_topic.topic_arn
    self.catalog_batch_process = _lambda.Function(
      self, 'CatalogBatchProcess',
      runtime=_lambda.Runtime.PYTHON_3_11,
      code=_lambda.Code.from_asset('product_service/lambda_func/'),
      handler='catalog_batch_process.handler',
      environment=environment
    )

    self.catalog_batch_process.add_event_source(event_source)
    catalog_items_queue.grant_consume_messages(self.catalog_batch_process)
    create_product_topic.grant_publish(self.catalog_batch_process)