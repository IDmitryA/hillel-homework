import random
from flask import Flask, request
from datetime import datetime


app = Flask(__name__)


@app.route('/whoami/')
def whoami():
    browser = ''
    chrome = "data:image/jpeg;base64,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"
    opera = "data:image/jpeg;base64,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"
    firefox = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTM6sOjH4HdRnV4at5sVr9gE6okSfj5y4MhHg&usqp=CAU"
    ip_address = request.remote_addr

    # I checked only on Chrom, in case of Opera and Firefox "request.user_agent.browser" values may differ
    # from "opera" and "firefox". Please don't consider as a mistake.

    if request.user_agent.browser == 'chrome':
        browser = chrome
    elif request.user_agent.browser == 'opera':
        browser = opera
    elif request.user_agent.browser == 'firefox':
        browser = firefox
    current_date_time = datetime.now()
    current_time = current_date_time.time()
    return f'''
<html>
    <title>
    Homework №7
    </title>
    <head>
    <img src="{browser}"/> <br/>

    user's IP: {ip_address} <br/>
    current time {current_time}
    </head>
</html>
'''


@app.route('/source_code/')
def source_code():
    f = open('dz7.py')
    return f'''
    <html>
        <title>
        Homework №7
        </title>
        <head>
        My code: <br/>
        {f.read()}
        </head>
    </html>
    '''


@app.route('/random/')
def rand():
    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_list = ['!', '"', '№', ';', '%', ':', '?', '*', '(', ')', '_', '+']
    digits_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    length = request.values.get('length', default='0')
    specials = request.values.get('specials', default='0')
    digits = request.values.get('digits', default='1')

    if int(specials):
        letters_list.extend(special_list)
    if int(digits):
        letters_list.extend(digits_list)
    result = ','.join(random.choice(letters_list) for _ in range(int(length)))

    if not 0 <= int(length) <= 100:
        result = 'Wrong input:<br/> "length" should be between 0 and 100'

    return f'''
    <html>
        <title>
        Homework №7
        </title>
        <head>
        <!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        <!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
        <form>
        Length: <br/>
        <input name="length" />
        <br/>
        Specials: <select class="form-select" aria-label="Default select example" input name="specials">
                  <option selected>Add special symbols?</option>
                  <option value="0">No</option>
                  <option value="1">Yes</option>
                  </select>
        <br/>
        Digits: <select class="form-select" aria-label="Default select example" input name="digits">
                  <option selected>Add digits?</option>
                  <option value="0">No</option>
                  <option value="1">Yes</option>
                  </select>
        <br/>
        <input type="submit" value="Get string"/>
        </form>
        {result}
        </head>
    </html>
    '''


app.run(debug=True)

