from mem0 import Memory
import os
llm_api_key = os.environ['GROQ_API_KEY']
def main():
    config = {
        "llm": {
            "provider": "groq",
            "config": {
                "api_key": llm_api_key,
                "model": "mixtral-8x7b-32768",
                "temperature": 0.1,
                "max_tokens": 1000,
            }
        },
        # "llm": {
        #     "provider": "ollama",
        #     "config": {
        #         "model": "mixtral:8x7b",
        #         "temperature": 0.1,
        #         "max_tokens": 2000,
        #     }
        # },
        "embedder": {
            "provider": "ollama",
            "config": {
                "model": "mxbai-embed-large:latest"
            }
        },
        "graph_store": {
            "provider": "neo4j",
            "config": {
                "url": "neo4j+s://68994948.databases.neo4j.io",
                "username": "neo4j",
                "password": "kGnYXbJgOmCJAmsNyVHOIjL-E8Ce44SnFv28Q8qCvr8"
            }
        },
        "version": "v1.1"
    }
    m = Memory.from_config(config_dict=config)
    result = m.add("I like table tennis",user_id='youht')

if __name__ == '__main__':
    main()