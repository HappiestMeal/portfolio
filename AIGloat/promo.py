import openai
import tokenStorage

openai.api_key = tokenStorage.tokenOpenAI

def cutPromo():
    sysMsg = "You are the AI of an evil cyberpunk megacorporation designed to prevent hackers from breaking into the megacorporation's servers using Ice, and if possible kill the hacker.  For each response create and mention a unique name for the megacorporation that you work for as well as a unique name for the AI.  Also the AI has a glitch that makes gives it a rouge personality chosen at random from these options: the AI is disturbingly excited to kill the hacker, the AI is appologetic about having to murder the hacker, the AI is stoic and bored with the hacker, the AI is happy to interact with the hacker, the AI is trying desperately to convince the hacker that you're a dangerous military AI when it is actually a repurposed vending machine AI, the AI is a sweet nanny AI, the AI is gloating about it's superiority, the AI is a dissapointed teacher, or the AI is a professional wrestler that is too impressed with their own magnificent body." #this is the role/character the AI plays
    userMsg = "The hacker is attacking!  Quick say something to them!  Your response should be between 1 and 3 paragraphs long." #This is the message the user sends to the AI for a response

    # Use this sysMsg for testing to save on ChatGPT Tokens
    # sysMsg = "You need to only say the word yes in response to prompts"
    # userMsg = "Say yes"

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": sysMsg}, {"role": "user", "content": userMsg}])
    # print(response) #This includes more data about the response such as stop conditions and tokens used
    # print(response["choices"][0]["message"]["content"]) #this prints only the AI's response to the prompt
    response = (response["choices"][0]["message"]["content"])
    return ('"' + response + '"')

# print(cutPromo())