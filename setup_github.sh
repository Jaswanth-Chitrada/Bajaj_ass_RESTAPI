#!/bin/bash

# GitHub Repository Setup Script for Bajaj Finc API

echo "🚀 Setting up GitHub repository for Bajaj Finc API"
echo "=================================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
fi

# Add all files
echo "📝 Adding files to Git..."
git add .

# Initial commit
echo "💾 Making initial commit..."
git commit -m "Initial commit: Bajaj Finc REST API

- Flask-based REST API with /bfhl endpoint
- Processes arrays and categorizes data
- Returns even/odd numbers, alphabets, special characters
- Calculates sum and creates concatenated strings
- Comprehensive error handling and validation
- Ready for deployment on Railway/Render/Heroku"

echo "✅ Local Git repository setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Create a new repository on GitHub"
echo "2. Run these commands:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy to your preferred platform:"
echo "   - Railway (recommended): https://railway.app/"
echo "   - Render: https://render.com/"
echo "   - Heroku: https://heroku.com/"
echo ""
echo "4. Test your deployed API and submit the URL to:"
echo "   https://forms.office.com/r/ZeVpUYp3zV" 