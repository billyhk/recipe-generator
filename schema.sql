drop table if exists ingredients;
drop table if exists recipes;
create table recipes(
    id serial primary key,
    name varchar(255) not "null",
    recipe_api_id integer
);
create table ingredients(
    id serial primary key,
    name varchar(255) not "null",
    ingredient_api_id integer
);