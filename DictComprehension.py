"""Dictionary Comprehension examples
"""

"""Before getting into Dict comprehension please learn about zip function
"""
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

z = zip(names, heros)
print(list(z))


"""Dictionary comprehension example
"""

name_hero_dict = {name:hero for (name, hero) in zip(names,heros) if(name != 'peter')}

print(name_hero_dict)