import ollama

def create_story(url):
    
    query = """
    Peux-tu écrire une histoire pour enfants inspirée de l'image. 
    Ecris l'histoire en français. 
    """

    res = ollama.generate(
        model="llava",
        prompt=query,
        images=[url]
    )
    
    return res['response']