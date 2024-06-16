import json

def handler(event, context):
  products = [
    {"id": "1", "name": "Terraforming Mars", "price": 35, "img": "../assets/terraforming-mars.jpg"},
    {"id": "2", "name": "Wingspan", "price": 40, "img": "../assets/wingspan.jpg"},
    {"id": "3", "name": "Everdell", "price": 45, "img": "../assets/everdell.jpg"},
    {"id": "4", "name": "Ticket to Ride", "price": 47, "img": "../assets/ticket-to-ride.jpg"},
    {"id": "5", "name": "Carcassonne", "price": 25, "img": "../assets/carcassonne.jpg"},
    {"id": "6", "name": "7 Wonders Duel", "price": 20, "img": "../assets/7-wonders-duel.jpg"},
    {"id": "7", "name": "Dune: Imperium", "price": 40, "img": "../assets/dune-imperium.jpg"},
  ]
  product_id = event["pathParameters"]["productId"]
  product = next((p for p in products if p["id"] == product_id), None)
  if product:
    return {
    "statusCode": 200,
    "headers": {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
      "content-type": "application/json"
    },
    "body": json.dumps(product)
  }
  else:
    return {
    "statusCode": 404,
    "headers": {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
      "content-type": "application/json"
    },
    "body": json.dumps("'message': 'Product not found'")
  }