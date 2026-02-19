from my_secrets import my_username

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "robot" in user_message or user_message == "hello, how are you doing" or "what is zeke's full name" or "where is keo" or "what class am i in right now" or "how are you doing this fine morning":
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""




def respond(user_message, user_name):
  if user_name == "Keo":
    bot_message = "be quiet nerd"
  else:
    bot_message = user_message
  if user_message == "hello, how are you doing":
    bot_message = "I'm doing splendiferously, how about you?"
  if user_message == "what is zeke's full name":
    bot_message = "Ezekial Leslie Johnson the 3rd"
  if user_message == "where is keo":
    bot_message = "not sure, he never comes to school fr"
  if user_message == "what class am i in right now":
    bot_message = "computer science"
  if user_message == "how are you doing this fine morning":
    bot_message = "quite splendiferously, you?"









  return f"""
  {bot_message.replace("robot", user_name)}"""




