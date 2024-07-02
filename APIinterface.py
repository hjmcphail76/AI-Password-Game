import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.0-pro-latest')

generateRequirementString = "Generate a password creation requirement that the user can use to modify the password, like a certain number of letters, numbers, and symbols.(One at a time though.) Make it actualy possible. Return only ONE requirement. The user just entered '{one}'and it needs critiquing."
def makeRequirement(previous):
    return model.generate_content(generateRequirementString.format(one = previous)).text

def check(string):
    return model.generate_content(string).text