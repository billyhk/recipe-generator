f = open('massData.json', 'r')
string = f.read()
dict = eval(string)

for recipe in dict['results']:
    for ingredient in recipe['missedIngredients']:
        
        print(f"insert into bridge (ingredient_api_id, recipe_api_id) values ('{ingredient['id']}', {recipe['id']});")