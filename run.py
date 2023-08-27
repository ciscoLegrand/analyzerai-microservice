import os
from app import create_app

ENVIRONMENT = os.getenv('ENVIRONMENT', 'default')
app = create_app(ENVIRONMENT)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
