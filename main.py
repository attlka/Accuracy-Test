import os
import openai
openai.api_key = os.getenv("gptkey")
openai.Answer.create(
  search_model="ada",
  model="babbage",
  question="What are the branches of philosophy?",
  documents=["sampledoc.pdf"],
	examples_context="Babylonian Philosophy is an example of bilingual intellectual culture."
	examples=[["What is an example of bilingual intellectual culture?","Babylonian Philosophy."]],
  max_tokens=70,
  stop=["\n", "<|endoftext|>"],
)
