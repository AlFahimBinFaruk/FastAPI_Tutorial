import uvicorn
from main import app

# run the server
if __name__ == "__main__":
    uvicorn.run(app=app,host="localhost",port=8000)