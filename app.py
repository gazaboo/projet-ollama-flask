from flask import Flask, render_template
import glob
from utils import create_story

# __name__ : double underscore variables (dunders)
app = Flask(__name__) 

@app.route("/")
def hello_world():
    urls = glob.glob('static/images/*.jpg')
    
    image_path_and_stories = []
    for url in urls:
        story = create_story( urls )
        url_html = '../' + url
        image_path_and_stories.append( (story, url_html) )

    return render_template('index.html', stories=image_path_and_stories)
 

app.run(debug=True, port=5000)

