#https://github.com/mandrewcito/signalrcore
import logging
import sys
sys.path.append("./")
from signalrcore.hub_connection_builder import HubConnectionBuilder

server_url = "ws://164.132.165.220:4004/assistanthub"

def login_function():
  return "dasdsa"

hub_connection = HubConnectionBuilder()\
    .with_url(server_url,options={"verify_ssl": False,"headers": {"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMmNkYTYxMC1kNzBhLTRkYTUtYTg2ZS1kMTRhYmMxN2JmYjIiLCJuYmYiOjE2NzY0Njk1ODYsImV4cCI6MTY3ODE5NzU4NiwiaWF0IjoxNjc2NDY5NTg2LCJpc3MiOiJaaXR1cmUiLCJhdWQiOiJaaXR1cmUifQ.PK8Gt0poa4rol8i9zovZHQ6zbHyNe2gl8zvYkbBQv34"}})\
    .with_automatic_reconnect({
            "type": "interval",
            "keep_alive_interval": 10,
            "intervals": [1, 3, 5, 6, 7, 87, 3]
        }).build()

hub_connection.on_open(lambda: print("connection opened and handshake received ready to send messages"))
hub_connection.on_close(lambda: print("connection closed"))

hub_connection.on("ReceiveMessage", print)
hub_connection.start()
message = None

# Do login

while message != "exit()":
    message = input(">> ")
    if message is not None and message != "" and message != "exit()":
        hub_connection.send("SendMessage")

hub_connection.stop()

sys.exit(0)