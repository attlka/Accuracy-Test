import os
import openai
openai.api_key = os.getenv("gptkey")

openai.File.create(file=open("sampledoc.pdf"), purpose='answers')

openai.Answer.create(
  search_model="davinci",
  model="davinci",
  question="What is the primary investigation of ethics?",
  documents=["sampledoc.pdf"],
  examples_context="Babylonian Philosophy is an example of bilingual intellectual culture.",
  examples=[["What is an example of bilingual intellectual culture?","Babylonian Philosophy."]],
  max_tokens=70,
  stop=["\n", "<|endoftext|>"],
)