import google.generativeai as genai
import os

os.environ["GEMINI_API_KEY"]="PUT_YOUR_KEY_HERE!"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,

)
model = genai.GenerativeModel('gemini-1.5-flash')
checkPasswordPrompt = "Check the following text: '{text1}' To see if it includes/meets the following requirement/suggestion found in the following text: {text2}. Return ONLY the words true or false, nothing else before or after. Give quite a bit of slack for the user, not too strict when checking."
makeRequirementPrompt = "Make a requirement to make this password more secure: '{text1}'. Suggest a SINGLE improvement to this password, word it like a requirement to continue. Be specific, but do not give the answer. Make sure what you are suggesting is actually possible to do by the user. No add this or that, only ONE. Nothing but the suggestion. Make the requirement logical and possible"
roastPrompt = "Now roast the password: '{text1}' and mostly the user for unrelated things. be funny and rude. do not repeat jokes from the chat. funny: 10/10 with sarcasim. Threaten to take over the world. no bad words."
chat_session = model.start_chat(
  history=[
  ]
)

def getHistory():
    return chat_session

def makeRequirement(previous):
    while True:
        try:
            return chat_session.send_message(makeRequirementPrompt.format(text1 = previous)).text
        except:
            pass

def check(previous, requirement):
    while True:
        try:
            return chat_session.send_message(checkPasswordPrompt.format(text1 = previous, text2 = requirement)).text
        except:
            pass

def roast(previous):
    while True:
        try:
            return chat_session.send_message(roastPrompt.format(text1 = previous)).text
        except:
            pass