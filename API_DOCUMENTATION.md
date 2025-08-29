# Bajaj Finc API Documentation

## Overview

The Bajaj Finc API is a REST API that processes arrays containing various data types (numbers, alphabets, special characters) and returns categorized results with additional computed values.

## Base URL

```
https://your-deployed-url.com
```

## Endpoints

### POST /bfhl

Processes an array of data and returns categorized results.

#### Request

**Method:** `POST`  
**Content-Type:** `application/json`

**Request Body:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

#### Response

**Status Code:** `200 OK`  
**Content-Type:** `application/json`

**Response Body:**
```json
{
  "is_success": true,
  "user_id": "john_doe_29082025",
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

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `is_success` | boolean | Status of the operation (true/false) |
| `user_id` | string | User ID in format: `full_name_ddmmyyyy` |
| `email` | string | User's email address |
| `roll_number` | string | College roll number |
| `odd_numbers` | array | Array of odd numbers (as strings) |
| `even_numbers` | array | Array of even numbers (as strings) |
| `alphabets` | array | Array of alphabets (converted to uppercase) |
| `special_characters` | array | Array of special characters |
| `sum` | string | Sum of all numbers (returned as string) |
| `concat_string` | string | Concatenated alphabets in reverse order with alternating caps |

#### Error Responses

**400 Bad Request - Missing Data Field:**
```json
{
  "is_success": false,
  "error": "Missing 'data' field in request body"
}
```

**400 Bad Request - Invalid Data Type:**
```json
{
  "is_success": false,
  "error": "'data' must be an array"
}
```

**500 Internal Server Error:**
```json
{
  "is_success": false,
  "error": "An error occurred: [error details]"
}
```

### GET /

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "message": "Bajaj Finc API is running",
  "endpoint": "/bfhl (POST)"
}
```

## Data Processing Logic

### Number Classification
- **Even Numbers:** Numbers divisible by 2
- **Odd Numbers:** Numbers not divisible by 2
- **Sum Calculation:** Sum of all numeric values

### Alphabet Processing
- **Uppercase Conversion:** All alphabets are converted to uppercase
- **Concatenation:** All alphabets are concatenated in reverse order with alternating caps

### Special Character Detection
- Single characters that are not alphanumeric

## Examples

### Example 1: Mixed Data Types

**Request:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_29082025",
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

### Example 2: Multiple Special Characters

**Request:**
```json
{
  "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_29082025",
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

### Example 3: Alphabets Only

**Request:**
```json
{
  "data": ["A", "ABcD", "DOE"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_29082025",
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

## Testing

### Using curl

```bash
curl -X POST https://your-api-url.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a", "1", "334", "4", "R", "$"]}'
```

### Using Python requests

```python
import requests

url = "https://your-api-url.com/bfhl"
data = {"data": ["a", "1", "334", "4", "R", "$"]}

response = requests.post(url, json=data)
print(response.json())
```

### Using JavaScript fetch

```javascript
fetch('https://your-api-url.com/bfhl', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    data: ["a", "1", "334", "4", "R", "$"]
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Rate Limiting

Currently, no rate limiting is implemented. However, it's recommended to implement rate limiting for production use.

## CORS

The API supports Cross-Origin Resource Sharing (CORS) and can be accessed from web browsers.

## Deployment

The API is designed to be deployed on various platforms:
- Railway
- Render
- Heroku
- Vercel
- Any platform supporting Python/Flask applications

## Support

For issues or questions, please refer to the project repository or contact the development team. 