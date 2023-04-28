from flask import Flask, request, Response

app = Flask(__name__)

header = None


@app.route('/echo')
def echo():
    text = request.args.get('message')
    if text and len(request.args) == 1:
        resp = Response(text, status=200)
        if header:
            resp.headers['banner'] = header
        return resp
    else:
        return 'None', 406


@app.route('/set_banner', methods=['POST'])
def set_banner():
    global header
    if request.method == 'POST':
        if request.headers.get("admin-auth") == "1234" and len(
                request.form) == 1:
            banner = request.form.get('banner')
            resp = Response(banner, status=200)
            header = banner
            return resp
        else:
            return 'None', 403


# main driver function
if __name__ == '_main_':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)