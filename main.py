from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radus: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
<body>
    <form method='POST'>
            <label>Rotate by:</label>
            <input type="text" name="rot" value="0" />
            <textarea name="text">{0}</textarea>
            <input type="submit" value="Submit Button" />            
    </form>
</body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rots = int(request.form['rot'])
    msg = request.form['text']
    #e_msg = rotate_string(msg, rots)
    return form.format(rotate_string(msg, rots))

app.run()