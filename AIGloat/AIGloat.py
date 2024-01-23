# Russ P.
# 08/15/23
# This code is just me playing around and making a twitch chat bot for learning purposes.  The code will take an input from twitch chat, generate a response from ChatGPT, and then read that response out loud in TTS

import time
import threading
import queue

from twitchio.ext import commands
from playSound import playSound
import promo
import tts
import tokenStorage

#This is a variable we are going to use to keep people from spamming a command in chat 
global timeOut 
timeOut = False

# This code was copy and pasted
class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=tokenStorage.tokenTwitchIO, prefix='!', initial_channels=[tokenStorage.channelName])

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g !hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')
        print("test")

    @commands.command(name="promo")
    async def promo(self, ctx: commands.Context):
        global timeOut
        if timeOut == False:
            try:
                timeOut = True
                change_queue.put(timeOut)

                x = promo.cutPromo()
                time.sleep(1)

                print(x)
                tts.getVoice(x)

                time.sleep(1)
                playSound()

                return timeOut
                
            except TypeError: #It's throwing a type error for checking the length of a NoneType, this handles that
                return
            
        else:       
            await ctx.send(f'{ctx.author.name}, there is a 5 minute wait between "promo" activations!')

# Create a queue to store the timeOut changes
change_queue = queue.Queue()

# Function that waits for the timeOut to change and then activates code
def restTimer():
    global timeOut
    while True:
        timeOut_change = change_queue.get()  # Wait for a timeOut change
        if timeOut_change:  # If timeOut changes to True
            # The code to be executed when timeOut becomes True
            time.sleep(300)
            timeOut = False
        else:  # If timeOut changes to False
            # The code to be executed when the timeOut becomes False
            print("timeOut is now False.")

thread = threading.Thread(target=restTimer)
thread.start()

def streamOver():
    thread.join() #We want to terminate the thread when we are done with it, but we will be using it all stream so run this command at the end of the stream to terminate.  If you forget just restart your PC.

bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.