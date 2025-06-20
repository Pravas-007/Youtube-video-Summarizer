**YouTube Video Summarizer (Python + Hugging Face)**
Python project to fetch YouTube transcripts and generate AI-based summaries.
This Python app fetches the transcript from any YouTube video and summarizes it using a transformer-based model (`facebook/bart-large-cnn`) from Hugging Face.

**Features:-**

- Enter a YouTube video URL
- Automatically fetch the transcript
- Summarize it using a pre-trained transformer model
- Display the output summary in terminal

**Tech Stack:-**

- Python 3
- Hugging Face Transformers
- `youtube-transcript-api`
- `facebook/bart-large-cnn` model

**Requirements:-**
Install the required packages
- youtube-transcript-api
- transformers
- torch
- sentencepiece
- tf-keras

**How to use:-**
Run the script: python summarizer.py

Example URL: https://www.youtube.com/watch?v=UwsrzCVZAb8

**Disclaimer:-**
This is a beginner-level AI project built for learning purposes.
Output quality depends on:
- The availability and clarity of the transcript (Only works for videos that have an auto-generated or manually uploaded transcript)
- The language (currently works best for English)
- The model’s generalization ability — summarization is based on pretrained behavior, not topic-specific training
May Not Work Well For:
- Music videos or songs
- Gaming/ASMR/memes with little or no speech
- Highly technical videos with poor transcription
- Non-English videos (unless manually transcribed)

**Author:-** 
Pravas Nayak
- This project was built as part of my early journey into Artificial Intelligence and Python development.
- It focuses on applying Natural Language Processing (NLP) to summarize YouTube videos, showcasing how AI can help distill large content into digestible insights.
- This tool was developed purely for educational and exploration purposes.
- It reflects the learning process of building real-world AI utilities with minimal resources.
