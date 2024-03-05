# Spotify Q&A Chatbot Engine

Welcome to the Spotify Q&A Chatbot Engine! 🎶🤖

## Overview
This innovative chatbot is designed to help you navigate through the vast world of Spotify, making music exploration 
and discovery a breeze. Powered by Google Review insights and state-of-the-art natural language processing, 
our chatbot provides personalized recommendations, answers your burning questions about artists, albums, playlists, 
and much more!

## 🚀 Try It Out!
- Install all the dependency in requirements.txt
- Set OPENAI_API_KEY in your environment variable if you don't have supported local model.
- You can put the [SPOTIFY_REVIEWS.csv](https://drive.google.com/file/d/1_xaRB6d2K_9-1dUmdU0GjtaqPO7uQnTM/view) in the .data/raw_data
  if you want to do the data preprocessing.
- You also can put the vector_storage folder into .data folder to prevent the app from building the vector storage from the beginning. Put this files to vector_storage folder:
  - [default__vector_store.json](https://drive.google.com/uc?export=download&id=1EtJl00YEwCboo_70GxPRi0Yc8ebqkoJl)
  - [docstore.json](https://drive.google.com/uc?export=download&id=1frN2BTjAmJkLMp9WIVtblEXX0xZIID7_)
  - [graph_store.json](https://drive.google.com/uc?export=download&id=1mqQhnXWcditdOJgWypDegF-FJskqfXF5)
  - [image__vector_store.json](https://drive.google.com/uc?export=download&id=1KwYZt8qn8CDjKiB8c1kod0P0sf1m58b_)
  - [index_store.json](https://drive.google.com/uc?export=download&id=13KhWmqUOHmbBfjx7mqCc6_3WCDvMEuPT)
- Run streamlit from server.py
```bash
streamlit run server.py
```

## Configuration
This app support local model. 
Can use all embedding model from huggingface.
insert the name of the model in [repository/main.py](https://github.com/benyamindariadi/Spotify-QA-Chatbot-Engine/blob/e6f48ce8e16096e1c783d70ac068814e4ddb5d1c/repository/main.py#L15)
```bash
self.embed_model_name = put_your_model_name_here
```
For LLM model this app support LlamaCPP so put the model directory in [repository/main.py](https://github.com/benyamindariadi/Spotify-QA-Chatbot-Engine/blob/e6f48ce8e16096e1c783d70ac068814e4ddb5d1c/repository/main.py#L18C9-L18C73)
```bash
self.llm_model_path = put_your_model_directory
```

## 📚 Examples
https://github.com/benyamindariadi/Spotify-QA-Chatbot-Engine/assets/57475499/a323dc5b-fb77-48df-bbc5-cb1fb7003037

https://github.com/benyamindariadi/Spotify-QA-Chatbot-Engine/assets/57475499/11db869b-ff43-41ed-9f76-e91c9e8d6397

https://github.com/benyamindariadi/Spotify-QA-Chatbot-Engine/assets/57475499/46ac570e-7783-46b1-8fd7-345dd0593f0c

https://github.com/benyamindariadi/Spotify-QA-Chatbot-Engine/assets/57475499/2684fc25-e9e6-4296-9bde-0578284d8d40
