f = open('massData.json', 'r')
string = f.read()
dict = eval(string)

for recipe in dict['results']:
    print(f"insert into recipes (name, recipe_api_id) values ('{recipe['title']}', {recipe['id']});")
