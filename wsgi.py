#!/usr/bin/env python3
import os
import sys
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

logger.info(f"🚀 WSGI startup - Current directory: {current_dir}")
logger.info(f"🚀 WSGI startup - Python path: {sys.path}")
logger.info(f"🚀 WSGI startup - Environment PORT: {os.environ.get('PORT', 'Not set')}")
logger.info(f"🚀 WSGI startup - Files in directory: {os.listdir(current_dir)}")

main_py_path = os.path.join(current_dir, 'main.py')
if not os.path.exists(main_py_path):
    logger.error(f"❌ main.py not found at {main_py_path}")
    raise FileNotFoundError("main.py not found")

logger.info(f"✅ main.py found at {main_py_path}")

try:
    logger.info("📦 Importing main module...")
    import main
    logger.info("✅ main module imported successfully")
    
    app = None
    
    if hasattr(main, 'create_app'):
        logger.info("🏗️ Using create_app function...")
        app = main.create_app()
        logger.info("✅ Flask app created via create_app()")
    elif hasattr(main, 'app'):
        logger.info("📱 Using app variable...")
        app = main.app
        logger.info("✅ Flask app obtained via app variable")
    else:
        logger.error("❌ No app or create_app found in main module")
        logger.error(f"Available attributes: {dir(main)}")
        raise ImportError("No Flask app found in main module")
    
    if app is None:
        logger.error("❌ Flask app is None")
        raise ValueError("Flask app is None")
    
    logger.info(f"✅ Flask app type: {type(app)}")
    logger.info("🎉 Flask app created successfully!")
    
except Exception as e:
    logger.error(f"❌ Failed to create Flask app: {e}")
    import traceback
    logger.error(f"📋 Full traceback: {traceback.format_exc()}")
    raise

try:
    with app.test_client() as client:
        response = client.get('/')
        logger.info(f"🧪 Test request to /: {response.status_code}")
except Exception as e:
    logger.warning(f"⚠️ Test request failed: {e}")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"🚀 Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
