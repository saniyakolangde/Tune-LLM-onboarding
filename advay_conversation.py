from transformers import pipeline, Conversation

chatbot = pipeline(model="facebook/blenderbot-400M-distill")

conversation = Conversation("Hi, we're DeepNeuron")
conversation = chatbot(conversation)

print(conversation)

conversation.add_user_input("What do you do?")
conversation = chatbot(conversation)


print(conversation)