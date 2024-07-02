import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"]="API_KEY_HERE"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# ^ no, you can not have my temp API key :)
model = genai.GenerativeModel('gemini-1.5-flash')

checkPasswordPrompt = "Check the following text: '{text1}' To see if it includes/meets the following requirement/suggestion found in the following text: {text2}. Return ONLY the words true or false, nothing else before or after."
roastPassword = "Roast this password: '{text1}' for being insecure. Suggest a single improvement to this password, word it like a requirement to continue. Be specific, but do not give the answer. Make sure what you are requiring/suggesting is actually doable by the user. Use ** ** to enclose the actual prompt of what you want done and NOWHERE ELSE. Must be there though."

def makeRequirement(previous):
    
    while True:
        try:
            return model.generate_content(roastPassword.format(text1 = previous)).text
        except:
            pass

def check(previous, requirement):
    while True:
        try:
            return model.generate_content(checkPasswordPrompt.format(text1 = previous, text2 = requirement)).text
        except:
            pass

def roast(previous,requirement):
    while True:
        try:
            return model.generate_content(roastPassword.format(text1 = previous)).text
        except:
            pass