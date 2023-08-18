from flask import Flask
import random
import os

app = Flask(__name__)

@app.route('/')
def say_hello():
    hello = ""
    for letter in "hello":
        is_upper_case = random.choice([True, False])
        hello += letter.upper() if is_upper_case else letter
    print(f"Sending: {hello}")
    return hello

if __name__ == '__main__':
    port = int(os.environ.get('HELLO_SERVICE_PORT', 8088))
    app.run(host='0.0.0.0', port=port)
