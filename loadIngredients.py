f = open('massData.json', 'r')
string = f.read()
dict = eval(string)

for recipe in dict['results']:
    for ingredient in recipe['missedIngredients']:
        
        print(f"insert into ingredients (name, ingredient_api_id) values ('{ingredient['name']}', {ingredient['id']});")
