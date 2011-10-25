import bleach
import jinja2
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    dirty = request.args.get('input', None)
    if dirty:
        clean = jinja2.Markup(bleach.clean(dirty))
    else:
        clean = None

    return render_template('index.html', clean=clean)


if __name__ == '__main__':
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('-d', '--debug', action='store_true', default=False,
                      help='Run the server in debug mode.')
    parser.add_option('-p', '--port', action='store', default=8000, type='int',
                      help='Port to listen on.')
    opts, _ = parser.parse_args()

    app.debug = opts.debug
    app.run(port=opts.port)
