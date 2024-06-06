from dotenv import load_dotenv
import uvicorn
from api.api import app
from decouple import config

load_dotenv()


PORT = config('PORT')
HOST = '0.0.0.0' 

if __name__ == "__main__":
    uvicorn.run('api.api: app', host=HOST, port=PORT, reload=True)
