# Set your Cloudinary credentials
# ==============================
import json

import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary import CloudinaryImage
from dotenv import load_dotenv

load_dotenv()

# Import the Cloudinary libraries
# ==============================

# Import to format the JSON responses
# ==============================

# Set configuration parameter: return "https" URLs by setting secure=True
# ==============================
config = cloudinary.config(secure=True)

# Log the configuration
# ==============================
print(
    "****1. Set up and configure the SDK:****\nCredentials: ",
    config.cloud_name,
    config.api_key,
    "\n",
)
