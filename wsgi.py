#!/usr/bin/env python3
import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

logger.info(f"Starting Flask app from directory: {current_dir}")
logger.info(f"Python path: {sys.path}")
logger.info(f"Environment PORT: {os.environ.get('PORT', 'Not set')}")

try:
    logger.info("Importing main module...")
    import main
    logger.info("✅ main module imported successfully")
    
    if hasattr(main, 'create_app'):
        logger.info("Using create_app function...")
        app = main.create_app()
    elif hasattr(main, 'app'):
        logger.info("Using app variable...")
        app = main.app
    else:
        logger.error("❌ No app or create_app found in main module")
        raise ImportError("No Flask app found")
        
    logger.info("✅ Flask app created successfully")
    
except Exception as e:
    logger.error(f"❌ Failed to create Flask app: {e}")
    import traceback
    logger.error(f"Traceback: {traceback.format_exc()}")
    raise

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"🚀 Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
