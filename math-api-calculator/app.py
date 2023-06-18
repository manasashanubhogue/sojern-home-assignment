from flask import abort, Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def get_request_numbers_quantifiers():
    data = request.get_json()
    numbers = data.get('numbers', [])
    quantifier = data.get('quantifier')
   
    if not numbers or not quantifier:
        abort(400, 'Invalid request')

    return numbers, quantifier

@app.route('/min', methods=['POST'])
def min_number():
    numbers, quantifier = get_request_numbers_quantifiers()

    numbers.sort()
    min_numbers = numbers[:quantifier]
    return jsonify({'min_numbers': min_numbers})

@app.route('/max', methods=['POST'])
def max_number():
    numbers, quantifier = get_request_numbers_quantifiers()

    numbers.sort(reverse=True)
    max_numbers = numbers[:quantifier]
    return jsonify({'max_numbers': max_numbers})

@app.route('/avg', methods=['POST'])
def average():
    data = request.get_json()
    numbers = data.get('numbers', [])

    if not numbers:
        return jsonify({'error': 'Invalid request parameters'})

    avg = np.mean(numbers)
    return jsonify({'average': avg})


@app.route("/median", methods=["POST"])
def calculate_median():
    data = request.get_json()
    numbers = data.get("numbers", [])
    
    median = np.median(numbers)

    return jsonify({"median": median})

@app.route("/percentile", methods=["POST"])
def calculate_percentile():
    numbers, quantifier = get_request_numbers_quantifiers()

    sorted_numbers = sorted(numbers)
    # p/100*N 
    index = int(np.ceil((quantifier / 100) * len(sorted_numbers))) - 1
    result = sorted_numbers[index]

    return jsonify({"percentile": result})


if __name__ == '__main__':
    app.run(debug=True)