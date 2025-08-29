# Bajaj Finc REST API

A Python Flask REST API that processes arrays and categorizes data into different types (numbers, alphabets, special characters) with various operations.

## Features

- **POST /bfhl**: Main endpoint that processes arrays
- Categorizes data into even numbers, odd numbers, alphabets, and special characters
- Calculates sum of all numbers
- Creates concatenated string with alternating caps in reverse order
- Returns user ID in format: `full_name_ddmmyyyy`
- Comprehensive error handling and validation

## API Endpoint

### POST /bfhl

Processes an array of data and returns categorized results.

**Request Body:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## Setup Instructions

### Local Development

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd bajaj_finc
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Test the API:**
   ```bash
   curl -X POST http://localhost:5000/bfhl \
     -H "Content-Type: application/json" \
     -d '{"data": ["a", "1", "334", "4", "R", "$"]}'
   ```

### Deployment

#### Heroku
1. Create a Heroku account and install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create a new app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

#### Railway
1. Connect your GitHub repository to Railway
2. Railway will automatically detect the Python app and deploy it

#### Render
1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn app:app`

## Environment Variables

- `PORT`: Port number (default: 5000)

## Customization

Before deploying, update the following in `app.py`:
- `full_name` in `generate_user_id()` function
- `email` in the response
- `roll_number` in the response

## Testing Examples

### Example A
**Request:**
```json
{"data": ["a", "1", "334", "4", "R", "$"]}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

### Example B
**Request:**
```json
{"data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["5"],
  "even_numbers": ["2", "4", "92"],
  "alphabets": ["A", "Y", "B"],
  "special_characters": ["&", "-", "*"],
  "sum": "103",
  "concat_string": "ByA"
}
```

### Example C
**Request:**
```json
{"data": ["A", "ABcD", "DOE"]}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": [],
  "even_numbers": [],
  "alphabets": ["A", "ABCD", "DOE"],
  "special_characters": [],
  "sum": "0",
  "concat_string": "EoDdCbAa"
}
```

## Error Handling

The API includes comprehensive error handling for:
- Missing or invalid request data
- Non-array input
- Server errors
- Invalid endpoints
- Unsupported HTTP methods

## Technologies Used

- **Python 3.11**
- **Flask**: Web framework
- **Flask-CORS**: Cross-origin resource sharing
- **Gunicorn**: WSGI HTTP Server for production
- **Python-dotenv**: Environment variable management

## License

MIT License 
