# Deployment Guide

This guide will help you deploy the Bajaj Finc API to various hosting platforms.

## Quick Deploy Options

### 1. Railway (Recommended - Fastest)

1. **Fork/Clone this repository** to your GitHub account
2. **Go to [Railway](https://railway.app/)** and sign up with GitHub
3. **Click "New Project"** → "Deploy from GitHub repo"
4. **Select your repository** and Railway will automatically detect it's a Python app
5. **Deploy** - Railway will automatically install dependencies and start the app
6. **Get your URL** - Railway will provide a URL like `https://your-app-name.railway.app`
7. **Test your API** at `https://your-app-name.railway.app/bfhl`

### 2. Render

1. **Fork/Clone this repository** to your GitHub account
2. **Go to [Render](https://render.com/)** and sign up with GitHub
3. **Click "New"** → "Web Service"
4. **Connect your repository**
5. **Configure the service:**
   - **Name**: `bajaj-finc-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. **Deploy** and get your URL
7. **Test your API** at `https://your-app-name.onrender.com/bfhl`

### 3. Heroku

1. **Install Heroku CLI** and login: `heroku login`
2. **Create a new app**: `heroku create your-app-name`
3. **Deploy**: `git push heroku main`
4. **Open your app**: `heroku open`
5. **Test your API** at `https://your-app-name.herokuapp.com/bfhl`

### 4. Vercel

1. **Fork/Clone this repository** to your GitHub account
2. **Go to [Vercel](https://vercel.com/)** and sign up with GitHub
3. **Import your repository**
4. **Configure build settings:**
   - **Framework Preset**: Other
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: `.`
   - **Install Command**: `pip install -r requirements.txt`
5. **Deploy** and get your URL
6. **Test your API** at `https://your-app-name.vercel.app/bfhl`

## Customization Before Deployment

Before deploying, update the following in `app.py`:

```python
# In the generate_user_id() function
full_name = "your_actual_name"  # Replace with your name in lowercase

# In the process_data() function response
"email": "your.email@example.com",  # Replace with your email
"roll_number": "YOUR_ROLL_NUMBER",  # Replace with your roll number
```

## Testing Your Deployed API

Once deployed, test your API with curl or any API testing tool:

```bash
curl -X POST https://your-app-url.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a", "1", "334", "4", "R", "$"]}'
```

Expected response:
```json
{
  "is_success": true,
  "user_id": "your_name_29082025",
  "email": "your.email@example.com",
  "roll_number": "YOUR_ROLL_NUMBER",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## Environment Variables

Most platforms will automatically set the `PORT` environment variable. If needed, you can set it manually:

- **Railway**: Set in the Variables tab
- **Render**: Set in the Environment section
- **Heroku**: `heroku config:set PORT=5000`
- **Vercel**: Set in the Environment Variables section

## Troubleshooting

### Common Issues:

1. **Port binding error**: The app automatically uses the `PORT` environment variable
2. **Dependencies not found**: Make sure `requirements.txt` is in the root directory
3. **App not starting**: Check the logs in your hosting platform's dashboard

### Health Check:

Test if your app is running by visiting the root URL:
```
https://your-app-url.com/
```

You should see:
```json
{
  "status": "healthy",
  "message": "Bajaj Finc API is running",
  "endpoint": "/bfhl (POST)"
}
```

## Submission

Once deployed, your API endpoint will be:
```
https://your-app-url.com/bfhl
```

Submit this URL to the form: https://forms.office.com/r/ZeVpUYp3zV 