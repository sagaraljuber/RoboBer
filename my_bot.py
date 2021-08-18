import discord
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys

driver = uc.Chrome()
driver.get('https://www.cleverbot.com')
driver.find_element_by_id('noteb').click()

def get_response(message):
    driver.find_element_by_xpath('//*[@id="avatarform"]/input[1]').send_keys(message + Keys.RETURN)
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="snipTextIcon"]')
            break
        except:
            continue
    response = driver.find_element_by_xpath('//*[@id="line1"]/span[1]').text
    return response

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author != self.user:
            reponse = get_response(message.content)
            await message.channel.send(f"{message.author.mention} {reponse}")

client = MyClient()
client.run('INSERT BOT TOKEN')

#Client ( our bot)
# client = commands.Bot(command_prefix='--')

# @client.command(name='version')
# async def version(context):

#     myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
#     myEmbed.add_field(name='Version Code:', value="v1.0.0", inline=False)
#     myEmbed.add_field(name="Date Released:", value="August 18,2021", inline=False)
#     myEmbed.set_footer(text="This is a sample footer")
#     myEmbed.set_author(name="Juber Sagaral")

#     await context.message.channel.send(embed=myEmbed)

# #stuff
# @client.event
# async def on_ready():

    
#     general_channel = client.get_channel(876072838463897603)
#     await general_channel.send('Hello, World!')

# @client.event
# async def on_message(message):
    
#     if message.content == 'what is the version':
#          general_channel = client.get_channel(876072838463897603)
         
#          myEmbed = discord.Embed(title="Current Version", description="The bot is in Version 1.0", color=0x00ff00)
#          myEmbed.add_field(name='Version Code:', value="v1.0.0", inline=False)
#          myEmbed.add_field(name="Date Released:", value="August 18,2021", inline=False)
#          myEmbed.set_footer(text="This is a sample footer")
#          myEmbed.set_author(name="Juber Sagaral")

         


#          await general_channel.send(embed=myEmbed)

#     await client.process_commands(message)


# #Run the client on the suerver



 