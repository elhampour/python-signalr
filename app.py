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

hub_connection.on("UserMessage", print)
hub_connection.on("ZitureMessage", print)
hub_connection.start()
message = None

# Do login

while message != "exit()":
    message = input(">> ")
    if message is not None and message != "" and message != "exit()":
        hub_connection.send("UserMessage",["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"])

hub_connection.stop()

sys.exit(0)