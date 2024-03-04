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
- Run streamlit from server.py
```bash
streamlit run server.py
```

## Configuration
This app support local model. 
Can use all embedding model from huggingface.
insert the name of the model in repository.main.py 
```bash
self.embed_model_name = put_your_model_name_here
```
For LLM model this app support LlamaCPP so put the model directory in repository.main.py 
```bash
self.llm_model_path = put_your_model_directory
```

## 📚 Examples
