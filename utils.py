import ollama

def create_story(url):
    
    query = """
    Peux-tu écrire une histoire pour enfants inspirée de l'image. 
    Ecris l'histoire en français. 
    Cette histoire doit être en alexandrins. 
    """

    res = ollama.generate(
        model="llava",
        messages=[
            {
                'role': 'user',
                'content': query,
                'images': ['static/images/1.jpg']
            }
        ]
    )

    return res['message']['content']