from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

hello_host = f"{os.environ['HELLO_SERVICE_HOST_PREFIX']}"
# world_host = f"{os.environ['WORLD_SERVICE_HOST_PREFIX']}.{os.environ['CONTAINER_APP_ENV_DNS_SUFFIX']}"

invoke_hello = f"{hello_host}"
# invoke_world = f"{world_host}/sayWorld"

@app.route("/")
def combine_greetings():
    hello_response = requests.get(invoke_hello)
    # world_response = requests.get(invoke_world)
    greeting = f"{hello_response.text}_world_tiger_{invoke_hello}"
    print(f"Sending: {greeting}")
    return greeting

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8090))
    app.run(host="0.0.0.0", port=port)
