from flask import Flask, render_template
import glob
import ollama
import os 

app = Flask(__name__) 

@app.route("/")
def hello_world():
    urls = glob.glob('static/images/*.jpg')
    abs_urls = [os.path.abspath(url) for url in urls]
    
    image_path_and_stories = []
    for url in abs_urls:
        story = create_story( url )
        url_html = 'images/' + url.split('/')[-1]
        image_path_and_stories.append( (story, url_html) )

    return render_template('index.html', stories=image_path_and_stories)

def create_story(url):
    query = """
    Peux-tu écrire une histoire pour enfants inspirée de l'image. 
    Ecris l'histoire en français. 
    """
    response = ollama.chat(model='gemma3:4b', messages=[{
        'role': 'user', 
        'content': query,
        'images': [url]
    }])
    return response['message']['content']

     
if __name__ == '__main__':
    app.run(debug=True, port=5000)
