# 🌐 Web-Based Google Sheets Translation Extractor

## 🚀 Local Server Setup (For Your Computer)

### Files You Need:
- `app.py` - Web application
- `templates/index.html` - Web interface  
- `requirements.txt` - Dependencies
- `setup.bat` - Setup script
- `server.bat` - Server launcher
- `credentials.json` - Your Google credentials

### Setup Steps:
1. **One-time setup:** Double-click `setup.bat`
2. **Start server:** Double-click `server.bat`
3. **Open browser:** Go to `http://localhost:5000`
4. **Use tool:** Click "Extract Translations" button

## ☁️ Deploy to Cloud (For Public Access)

### Option 1: Railway (Easiest)
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub account
3. Upload your project files (without `credentials.json`)
4. Add `credentials.json` content as environment variable
5. Deploy - you get a public URL!

### Option 2: Heroku
1. Create account at [heroku.com](https://heroku.com)
2. Install Heroku CLI
3. Create new app: `heroku create your-app-name`
4. Add credentials as config var in Heroku dashboard
5. Deploy: `git push heroku main`

### Option 3: Replit (Super Easy)
1. Go to [replit.com](https://replit.com)
2. Create new Python project
3. Upload all files
4. Add `credentials.json` content to Secrets tab
5. Click "Run" - instant deployment!

### Option 4: PythonAnywhere
1. Create account at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload files via dashboard
3. Set up web app with Flask
4. Configure environment variables

## 🔧 For Cloud Deployment

### Create a Procfile (for Heroku/Railway):
```
web: python app.py
```

### Update app.py for production:
```python
# Change last line to:
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

## 📱 User Experience

### What Users See:
1. **Beautiful web interface** - No downloads needed
2. **One-click extraction** - Just click a button
3. **Instant download** - JSON file downloads automatically
4. **Works on any device** - Phone, tablet, computer

### Example User Flow:
1. Visit your website
2. Click "Extract Translations"
3. Wait 5-10 seconds
4. Download JSON file
5. Done!

## 🎯 Benefits of Web Version

✅ **No software installation** for users  
✅ **Works on any device** (phone, tablet, laptop)  
✅ **Always up-to-date** - you control the server  
✅ **Professional appearance** - looks like a real app  
✅ **Easy sharing** - just send a link  
✅ **Error handling** - clear messages if something goes wrong  
✅ **Mobile friendly** - responsive design  

## 💰 Costs

- **Local server:** Free (runs on your computer)
- **Replit:** Free tier available
- **Railway:** Free tier (500 hours/month)
- **Heroku:** $7/month for basic plan
- **PythonAnywhere:** Free tier available

## 🚀 Recommended Approach

**For testing:** Use local server (`server.bat`)
**For sharing:** Deploy to Railway or Replit (easiest)
**For business:** Use Heroku or PythonAnywhere (more reliable)