from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import json
from pprint import pprint
app = Flask(__name__)


def getFoodsFromRecipe():
    with open('data_sources/recipes.json') as f:
        data = json.load(f)

        Foods = []

        for i in range(len(data)):

            recipe = data[i]
            ingredients = recipe["ingredients"]

            for j in range(len(ingredients)):

                food = ingredients[j]["food"]
                if food not in Foods:
                    Foods += [food]

        pprint(Foods)


def readBarcode():
    with open('data_sources/barcode.json') as f:
        barcode = json.load(f)
    return barcode


def readRecipe():
    with open('data_sources/recipes.json') as f:
        recipe = json.load(f)
    return recipe


def readPLU():
    with open('data_sources/plu.json') as f:
        plu = json.load(f)
    return plu

# saving barcode


@app.route('/barcode/<code>/<item>', methods=['POST'])
def saveBarcode(code, item):
    barcodes = readBarcode()
    print(code)
    print(item)
    if code not in barcodes:
        barcodes[code] = item
        with open('data_sources/barcode.json', 'w') as f:
            f.write(json.dumps(barcodes, sort_keys=True, indent=2))
            return item
    return ''


# getting barcode
@app.route('/barcode/<code>', methods=['GET'])
def getBarcode(code):
    barcodes = readBarcode()
    if code in barcodes:
        return barcodes[code]

# saving plu


@app.route('/plu/<code>/<item>', methods=['POST'])
def savePlu(code, item):
    plu = readPLU()
    if code not in plu:
        plu[code] = item
        with open('data_sources/plu.json', 'w') as f:
            f.write(json.dumps(plu, sort_keys=True, indent=2))


# getting plu
@app.route('/plu/<code>', methods=['GET'])
def getPlu(code):
    plu = readPLU()
    if code in plu:
        return plu[code]
    else:
        return "error"

# getting recipes


@app.route('/recipes', methods=['GET'])
def getRecipe():
    recipe = readRecipe()
    return jsonify(recipe)


if __name__ == "__main__":
    app.run()
