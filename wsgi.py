#!/usr/bin/env python3
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from main import create_app
    app = create_app()
    logger.info("✅ Flask app created successfully")
except Exception as e:
    logger.error(f"❌ Failed to create Flask app: {e}")
    raise

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"🚀 Starting Flask app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
