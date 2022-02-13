import random
from flask import Flask, request
from datetime import datetime


app = Flask(__name__)


@app.route('/whoami/')
def whoami():
    ip_address = request.remote_addr
    browser = request.user_agent.browser
    current_date_time = datetime.now()
    current_time = current_date_time.time()
    return f"User's browser: {browser.capitalize()}, user's IP: {ip_address}, current time {current_time}"


@app.route('/source_code/')
def source_code():
    f = open('dz4.py')
    return f.read()


@app.route('/random/')
def rand():
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_list = ['!', '"', '№', ';', '%', ':', '?', '*', '(', ')', '_', '+']
    digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    length = request.values.get('length')
    specials = request.values.get('specials', default='0')
    digits = request.values.get('digits', default='1')

    if not all([0 <= int(length) <= 100, 0 <= int(specials) <= 1, 0 <= int(digits) <= 1]):
        return f'Wrong input: "length" should be between 0 and 100, "specials" and "digits" should equal 0 or 1'

    if int(specials):
        letters_list.extend(special_list)
    if int(digits):
        letters_list.extend(digits_list)
    result = ','.join(random.sample(letters_list, int(length)))
    
    return result


app.run(debug=True)

