# Flask and Dash

how to frontend data science by yish.

### How to run the files

* in the terminal, just do `python run.py`
* through doing that, you might get a bunch of errors which'll point you towards what needs to be `pip install`'d


## Overview

### What is Flask?

* Flask is a web framework that supports the development of web applications
* for our purposes, to host our models on some frontend!

### How does Flask work?

* file architecture is annoyingly important here
* *caveat: this way is specific to incorporating Dash into your Flask app! Without Dash it's a little simpler but Dash is great for EDA!*


* `run.py`
* folder: `dash_package`
  * `init.py`
  * `routes.py`
  * subfolders:
    * `templates` (html stuff)
    * `static` (html stuff)
  * any other files would go inside `dash_package`

### Important files

1. `base-directory/dash_package/...`: this is the folder where you're going to put all your stuff in. if you have additional files with functions, etc., likely you put those here.

2. `base-directory/run.py`: this is the only file outside `dash_package`, and you use this to run your app. you're gonna need to have this code in there:

```
from dash_package import app

if __name__ == "__main__":
    app.run_server(debug=True)

```

3. `.../dash_package/__init__.py`: here's where you configure your server and your dash app. i don't know what that means either.

```
from flask import Flask
import dash

server = Flask(__name__)

server.config['DEBUG'] = True

app = dash.Dash(__name__, server=server, url_base_pathname='/dash/')
app.config['suppress_callback_exceptions']=True

from dash_package import routes
```

4. `.../dash_package/routes.py`: here's where you define your URLs and also what renders on the webpage at each URL. these are functions with decorators (no idea why)

```
@app.server.route('/dash')
def dashboard():
    return app.index()

@app.server.route('/hello')
def hello():
    return "Oh hello"
```


#### Kinda important files

5. `.../dash_package/dashboard.py`: this is where your code for your plotly dashboard goes

6. `.../dashboard/templates/...`: this is for any html templates you end up using on your app

7. `.../dashboard/static/...`: this is where you'd put things like images that you want to have within your html

### Putting your model on Flask

1. think about your inputs and outputs. how does your project take inputs and turn them into some result?

2. you need to script your functions into Python files and **pickle** the stuff you need (models, preprocessing tools - i.e. tfdif vectorizer)

3. in `routes.py`, your input page is where you made a `GET` request, and your output is where you have your `POST` request. in your `POST`, that's where you call on your model. the output also has to be a string to render on the webpage

```
@app.server.route('/model', methods = ['GET'])
def render_html():
    return render_template('classifier.html')

@app.server.route('/model', methods = ['POST'])
def predict():
    text = request.form.get('name')
    prediction = classify_text(text)
    return str(prediction)

```

4. `render_template` is a function you use to display your html. your html code goes into the `templates` folder and any files that you use in your html goes into the `static` folder.

5. html code is low-key the worst -- just google how to do everything lol

6. you have all my code for my web app, so just play around and figure it out! in `routes.py` and `functions.py` i have two versions of code (commented!) to show the difference between render_html and simple string outputs.
