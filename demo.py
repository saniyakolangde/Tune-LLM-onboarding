from transformers import pipeline, Conversation


classifier = pipeline(task="sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

print(classifier("DeepNeuron is amazing"))

#we can do feature extraction, summerisation, text generation, translation, question-answering