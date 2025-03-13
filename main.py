from dotenv import load_dotenv
from mem0 import MemoryClient
import os

load_dotenv()

client = MemoryClient(api_key=os.environ.get("MEM0_API"))

config = {
    "vector_store": {
        "provider": "supabase",
        "config": {
            "connection_string": "postgresql://user:password@host:port/database",
            "collection_name": "memories",
            "index_method": "hnsw",  # Optional: defaults to "auto"
            "index_measure": "cosine_distance"  # Optional: defaults to "cosine_distance"
        }
    }
}

messages = [
    {"role": "user", "content": "Hi, I'm Kritik. I'm a Non vegetarian and I'm allergic to squids."},
    {"role": "assistant", "content": "Hello Kritik! I've noted that you're a Non vegetarian and have a squid allergy. I'll keep this in mind for any food-related recommendations or discussions."}
]
client.add(messages, user_id="kritik")

# query = "What can I cook for dinner tonight?"
# client.search(query, user_id="kritik")