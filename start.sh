#!/bin/bash
echo "🔍 Render Startup Debug"
echo "Python version: $(python --version)"
echo "Current directory: $(pwd)"
echo "Files in directory:"
ls -la
echo "Environment variables:"
env | grep -E "(PORT|PYTHON|RENDER)"
echo "Testing Python imports:"
python -c "import main; print('✅ main.py import successful')"
python -c "from main import create_app; app = create_app(); print('✅ Flask app creation successful')"
echo "Starting gunicorn..."
exec gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --preload --log-level info --access-logfile - --error-logfile -
