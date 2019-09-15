import flask                                # Allows us to use Flask classes / methods.

app = flask.Flask("__main__")


@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Hello Flask+React")


app.run(debug=True)

## react_frontend

# index.html index that is rendered when we run our build

# npm eject: unpacks the paths.js and webpack.config.js