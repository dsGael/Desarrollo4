from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''<html>
                <head>
                    <title> HELLO </title>
                </head>
                <body>
                    <h1>Hello World!</h1>
                    <a href="/about">About </a>

                </body>

              </html>  
            
            ''' 

@app.route("/about") #about
def about():
 return '''<html>
                <head>
                    <title> About this page </title>
                </head>
                <body>
                    <h1>About</h1>
                    <p>Everything about hello world</p>
                    Back to <a href="/">Hello world! </a>


                </body>

              </html>  
            
            ''' 

if __name__ == '__main__':
   app.run(debug=True)