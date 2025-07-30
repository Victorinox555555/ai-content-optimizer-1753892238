
import sys
sys.path.insert(0, '/tmp/test_skill_output')

try:
    from main import create_app
    app = create_app()
    print("✅ Flask app import and creation successful")
    
    with app.test_client() as client:
        response = client.get('/')
        print("✅ Homepage test: " + str(response.status_code))
        
        response = client.get('/health')
        print("✅ Health check test: " + str(response.status_code))
        
except Exception as e:
    print(f"❌ Flask app test failed: {e}")
    raise
