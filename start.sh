#!/bin/bash
set -e

echo "🔍 === RENDER STARTUP DEBUG ==="
echo "📅 Timestamp: $(date)"
echo "🐍 Python version: $(python --version)"
echo "📂 Current directory: $(pwd)"
echo "📁 Files in directory:"
ls -la

echo ""
echo "🌍 Environment variables:"
env | grep -E "(PORT|PYTHON|RENDER|FLASK)" | sort

echo ""
echo "🧪 Testing Python imports:"
python -c "print('✅ Python basic import test passed')"

echo ""
echo "📦 Testing main.py import:"
python -c "
try:
    import main
    print('✅ main.py import successful')
    print(f'📋 main module attributes: {[attr for attr in dir(main) if not attr.startswith("_")]}')
    
    if hasattr(main, 'create_app'):
        app = main.create_app()
        print('✅ create_app() function works')
        print(f'📱 App type: {type(app)}')
    elif hasattr(main, 'app'):
        app = main.app
        print('✅ app variable accessible')
        print(f'📱 App type: {type(app)}')
    else:
        print('❌ No app or create_app found')
        
except Exception as e:
    print(f'❌ main.py import failed: {e}')
    import traceback
    traceback.print_exc()
"

echo ""
echo "🧪 Testing wsgi.py import:"
python -c "
try:
    import wsgi
    print('✅ wsgi.py import successful')
    print(f'📱 WSGI app type: {type(wsgi.app)}')
except Exception as e:
    print(f'❌ wsgi.py import failed: {e}')
    import traceback
    traceback.print_exc()
"

echo ""
echo "🚀 Starting gunicorn..."
exec gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --preload --log-level debug --access-logfile - --error-logfile - --capture-output --enable-stdio-inheritance
