from flask import Flask, request, render_template
from datetime import date, datetime
import requests

app = Flask(__name__)

@app.route("/")
def get_home():
    response = requests.get('http://localhost:5000/api/recipes/')
    if response.status_code == 200:
        return render_template('home.html', recipes=response.json())
    else:
        return "error"
    
@app.route("/recipe/<name>")
def get_one_recipe(name):
    url ='http://localhost:5000/api/recipes/name/{}/'.format(name)
    print(url)
    response = requests.get(url )
    print(response.status_code)
    if response.status_code == 200:
        return render_template('recipe.html', recipe=response.json())
    else:
        return "error"
    
@app.route("/recipe/add/", methods=['POST', 'GET'])
def add_recipe():
    if request.method == 'GET':
        
        return render_template('add_recipe.html')
    else:
        data = request.form
        tags = request.form.getlist('tags[]')
        ingredients = request.form.getlist('ingredients[]')
        steps = request.form.getlist('steps[]')
        print(tags)
        print(ingredients)
        print(steps)

        return data
    
@app.route("/recipe/search/", methods=['POST'])
def search_results():
    search_request = request.form.get('recipeSearch')
    url ='http://localhost:5000/api/recipes/search/{}/'.format(search_request)
    print(url)
    response = requests.get(url )
    print(response.status_code)
    if response.status_code == 200:
        return render_template('search.html', search_results=response.json())
    else:
        return "error"
    
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)