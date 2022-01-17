import flask

from utils import generate, read_time_uuid_file, save_time_uuid

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Welcome Cowrywise TimeUUID api.</h1><p>To get stored TimeUUID visit /gettimeuuid.</p><p> To generate TimeUUID visit /generate</p>"


@app.route('/gettimeuuid', methods=['GET'])
def get_time_uuid():
    data = read_time_uuid_file()
    return data, 201


@app.route('/generate', methods=['GET'])
def gen_time_uudi():
    data = generate()
    save_time_uuid(data)
    return data, 201


app.run()
