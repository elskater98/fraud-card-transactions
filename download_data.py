from dotenv import load_dotenv

import os
load_dotenv()

if __name__ == '__main__':
    token = os.environ.get("api-token")