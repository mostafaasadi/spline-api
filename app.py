import os
import ast
import uuid
from engine import draw
from flask import Flask, request, abort, send_file


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
        try:
            plot = draw(img='img/uploads/{}'.format(filename), tck=tck)
            return(send_file(plot, mimetype='image/gif'))
        except Exception:
            abort(500)


if __name__ == "__main__":
    app.run()
