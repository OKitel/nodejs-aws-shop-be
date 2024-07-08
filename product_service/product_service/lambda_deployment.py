from aws_cdk import Stack
from aws_cdk import aws_dynamodb as dynamodb
from product_service.api_gateway import ApiGateway
from product_service.get_product_by_id import ProductById
from product_service.get_products import GetProducts
from product_service.put_products import PutProducts
from product_service.catalog_batch_process import CatalogBatchProcess
from constructs import Construct

class MyCdkAppStack(Stack):
  def __init__(self, scope: Construct, id: str, **kwargs) -> None:
    super().__init__(scope, id, **kwargs)

    products_table_name = 'Products'
    stocks_table_name = 'Stocks'

    products_table = dynamodb.Table.from_table_name(self, 'ProductsTable', products_table_name)
    stocks_table = dynamodb.Table.from_table_name(self, 'StocksTable', stocks_table_name)

    environment = {
      "PRODUCTS_TABLE_NAME": products_table_name,
      "STOCKS_TABLE_NAME": stocks_table_name,
    }

    get_products_list_lbd = GetProducts(self, 'ProductsList', environment)
    get_product_by_id_lbd = ProductById(self, 'ProductByID', environment)
    put_products_lbd = PutProducts(self, 'PutProducts', environment)
    ApiGateway(self, 'APIGateway', get_products_list_fn=get_products_list_lbd.get_products_list, get_product_by_id_fn=get_product_by_id_lbd.get_product_by_id, put_products_fn=put_products_lbd.put_products)
    catalog_batch_process_lbd = CatalogBatchProcess(self, 'CatalogBatchProcess', environment)

    products_table.grant_read_write_data(get_products_list_lbd.get_products_list)
    stocks_table.grant_read_write_data(get_products_list_lbd.get_products_list)
    products_table.grant_read_write_data(get_product_by_id_lbd.get_product_by_id)
    stocks_table.grant_read_write_data(get_product_by_id_lbd.get_product_by_id)
    products_table.grant_read_write_data(put_products_lbd.put_products)
    stocks_table.grant_read_write_data(put_products_lbd.put_products)
    products_table.grant_read_write_data(catalog_batch_process_lbd.catalog_batch_process)
    stocks_table.grant_read_write_data(catalog_batch_process_lbd.catalog_batch_process)
    