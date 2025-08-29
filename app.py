from flask import Flask, request, jsonify
from flask_cors import CORS
import re
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

def generate_user_id():
    """Generate user_id in format: full_name_ddmmyyyy"""
    # You can customize this with your actual name
    full_name = "Jaswanth_Chitrada"  # Replace with your actual name in lowercase
    current_date = datetime.now()
    date_str = current_date.strftime("%d%m%Y")
    return f"{full_name}_{date_str}"

def is_number(string):
    """Check if a string represents a number"""
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_integer(string):
    """Check if a string represents an integer"""
    try:
        int(string)
        return True
    except ValueError:
        return False

def is_alphabet(string):
    """Check if a string contains only alphabets"""
    return string.isalpha()

def is_special_character(string):
    """Check if a string is a special character"""
    # Check if it's a single character and not alphanumeric
    return len(string) == 1 and not string.isalnum()

def process_array(data):
    """Process the input array and return categorized results"""
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_characters = []
    numbers_sum = 0
    all_alphabets = []
    
    for item in data:
        item_str = str(item)
        
        if is_number(item_str):
            if is_integer(item_str):
                num = int(item_str)
                numbers_sum += num
                if num % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
            else:
                # Handle decimal numbers
                num = float(item_str)
                numbers_sum += num
                if num % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
        elif is_alphabet(item_str):
            alphabets.append(item_str.upper())
            all_alphabets.extend(list(item_str))
        elif is_special_character(item_str):
            special_characters.append(item_str)
    
    # Create concatenated string with alternating caps in reverse order
    concat_string = ""
    for i, char in enumerate(reversed(all_alphabets)):
        if i % 2 == 0:
            concat_string += char.upper()
        else:
            concat_string += char.lower()
    
    return {
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(numbers_sum),
        "concat_string": concat_string
    }

@app.route('/bfhl', methods=['POST'])
def process_data():
    """Main endpoint to process array data"""
    try:
        # Get JSON data from request
        request_data = request.get_json()
        
        if not request_data or 'data' not in request_data:
            return jsonify({
                "is_success": False,
                "error": "Missing 'data' field in request body"
            }), 400
        
        data = request_data['data']
        
        if not isinstance(data, list):
            return jsonify({
                "is_success": False,
                "error": "'data' must be an array"
            }), 400
        
        # Process the array
        processed_data = process_array(data)
        
        # Prepare response
        response = {
            "is_success": True,
            "user_id": generate_user_id(),
            "email": "jaswanthchitrada45@gmail.com",  
            "roll_number": "22BCE3546",  
            "odd_numbers": processed_data["odd_numbers"],
            "even_numbers": processed_data["even_numbers"],
            "alphabets": processed_data["alphabets"],
            "special_characters": processed_data["special_characters"],
            "sum": processed_data["sum"],
            "concat_string": processed_data["concat_string"]
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": f"An error occurred: {str(e)}"
        }), 500

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Bajaj Finc API is running",
        "endpoint": "/bfhl (POST)"
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "is_success": False,
        "error": "Endpoint not found"
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "is_success": False,
        "error": "Method not allowed"
    }), 405

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 