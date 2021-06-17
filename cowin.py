import discord
from cowin_api  import CoWinAPI
from dotenv import load_dotenv
import os
load_dotenv('token_vaccine.env')

token = os.getenv('TOKEN')
cowin = CoWinAPI()



district_id = '141'

states = cowin.get_availability_by_district(district_id)
print(states['centers'][0]['name'])
for i in range(len(states['centers'])):

	centres = states['centers'][i]

	for j in range(len(centres['sessions'])):
		if centres['sessions'][j]['min_age_limit'] == 18:

			print(centres['name'] +"     "+str(centres['sessions'][j]['available_capacity_dose1']) + "      " + str(centres['sessions'][j]['date']) )


client = discord.Client()


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	await message.channel.send(f'{client.user} has joined')

	if message.content == 'show slots':
		for i in range(len(states['centers'])):

			centres = states['centers'][i]

			for j in range(len(centres['sessions'])):
				if centres['sessions'][j]['min_age_limit'] == 18:

					await message.channel.send(centres['name'] +"     "+str(centres['sessions'][j]['available_capacity_dose1']) + "      " + str(centres['sessions'][j]['date']) )

				


client.run(token)