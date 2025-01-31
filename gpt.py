"""
lets create a Chat-Gpt in python

anfd after we will create a chatgpt telegram-Bot

"""


from openai import OpenAI
import telebot

#I have stored open ai api and telegram bot token in config file u can put direct
api_key="Enter Open Ai api"
Bot_token="Enter your Bot token"

client=OpenAI(api_key=api_key)
bot=telebot.TeleBot(Bot_token)

messages=[{"role":"user","content":"You are shishya created by Shishya and his insta id is (Nexcrypt)"}]

#Chat-gpt function

def ask_gpt(prompt):
    messages.append({"role":"user","content":prompt})
    completetion=client.chat.completions.create(
        model="gpt-4o-mini", #Chose only gpt-40 mini
        messages=messages
    )
    return completetion.choices[0].message.content.strip()

#Now create a Bot function

@bot.message_handler(['start'])

def start(message):
    bot.reply_to(message,text="Hello Welcome to Bot\nYou can ask anyhting You wnat")

#Chat-Gpt function

@bot.message_handler(func= lambda message:True)

def send_message(message):
    prompt=message.text
    bot_reply= ask_gpt(prompt=prompt)
    bot.reply_to(message,bot_reply)
#at first lets check

print("Bot is runing...")
bot.polling()