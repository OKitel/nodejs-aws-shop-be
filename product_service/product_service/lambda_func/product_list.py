import json

BASE_URL = "https://d266s2h0r1qt2p.cloudfront.net/assets/img/"

def handler(event, context):
  products = [
    {"id": "1", "name": "Terraforming Mars", "price": 35, "img": f"{BASE_URL}terraforming-mars.jpg"},
    {"id": "2", "name": "Wingspan", "price": 40, "img": f"{BASE_URL}wingspan.jpg"},
    {"id": "3", "name": "Everdell", "price": 45, "img": f"{BASE_URL}everdell.jpg"},
    {"id": "4", "name": "Ticket to Ride", "price": 47, "img": f"{BASE_URL}ticket-to-ride.jpg"},
    {"id": "5", "name": "Carcassonne", "price": 25, "img": f"{BASE_URL}carcassonne.jpg"},
    {"id": "6", "name": "7 Wonders Duel", "price": 20, "img": f"{BASE_URL}7-wonders-duel.jpg"},
    {"id": "7", "name": "Dune: Imperium", "price": 40, "img": f"{BASE_URL}dune-imperium.jpg"},
  ]

  return {
    "statusCode": 200,
    "headers": {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET",
      "content-type": "application/json"
    },
    "body": json.dumps(products)
  }