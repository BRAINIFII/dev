from dotenv import load_dotenv
from mem0 import MemoryClient
import os

load_dotenv()

client = MemoryClient(api_key=os.environ.get("MEM0_API"))