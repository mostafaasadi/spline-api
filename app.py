import os
import ast
import uuid
from engine import draw
from flask import Flask, request, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_image():
    if request.method == 'POST':
        data = dict(request.form)
        if 'image' not in request.files:
            abort(400)
        file = request.files['image']
        if file.filename == '':
            abort(400)
        filename = uuid.uuid4().hex
        file.save(os.path.join('img/uploads', filename))
        if 'tck' not in data:
            abort(403)
        tck = ast.literal_eval(data['tck'])
        draw(img='img/uploads/{}'.format(filename), tck=tck)
        return('200')


if __name__ == "__main__":
    app.run()
