import json

SHORTFORM = {
    ("tbsp", "tablespoons"),
    ("Tbsp", "tablespoons"),
    ("tbls", "tablespoons"),
    ("Tbls", "tablespoons"),
    ("tb", "tablespoons"),
    ("Tb", "tablespoons"),
    ("T", "tablespoons"),
    ("tsp", "teaspoons"),
    ("ts", "teaspoons"),
    ("t", "teaspoons"),
    ("ml", "milliliters"),
    ("mL", "milliliters"),
    ("L", "liters"),
    ("fl oz", "fluid ounces"),
    ("fluid oz", "fluid ounces"),
    ("kg", "kilograms"),
    ("g", "grams"),
    ("mg", "milligrams"),
    ("lb", "pounds"),
    ("lbs", "pounds"),
    ("fluid oz", "fluid ounces"),
    ("c", "cups"),
    ("qt", "quarts"),
    ("pt", "pints")

}


VOLUME = {
    ("cups", "milliliters"): 236.59,
    ("liters", "milliliters"): 1000.0,
    ("fluid ounces", "milliliters"): 29.57,
    ("teaspoons", "milliliters"): 4.93,
    ("quarts", "milliliters"): 946.35,
    ("pints", "milliliters"): 473.18,

}

MASS = {
    ("milligrams", "grams"): 0.001,
    ("kilograms", "grams"): 1000.0,
    ("ounces", "grams"): 28.35,
    ("pounds", "grams"): 453.59,
    ("ton", "grams"): 907185.0,


}

json.dump(SHORTFORM, open("units_shortform.json","w"))
json.dump(VOLUME, open("units_volume.json","w"))
json.dump(MASS, open("units_mass.json","w"))

# with open("units_shortforms.json", "w") as fw:
#     fw.write(json.dumps(SHORTFORMS))
#
# with open("units_volume.json", "w") as fw:
#     fw.write(json.dumps(VOLUMES))
#
# with open("units_mass.json", "w") as fw:
#     fw.write(json.dumps(MASS))