import json

import sys
import os
import pytest

lambda_dir = os.path.dirname('../../product_service/lambda_func')
sys.path.append(lambda_dir)
from product_service.lambda_func import product_by_id

def test_handler_returns_product():
    event = {
        'pathParameters': {
            'productId': '1'
        }
    }
    response = product_by_id.handler(event, None)
    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['name'] == 'Terraforming Mars'
    assert body['price'] == 35

def test_handler_returns_404_for_nonexistent_product():
    event = {
        'pathParameters': {
            'productId': '100'
        }
    }
    response = product_by_id.handler(event, None)
    assert response['statusCode'] == 404
    body = json.loads(response['body'])
    assert body == "'message': 'Product not found'"

if __name__ == '__main__':
    pytest.main()

