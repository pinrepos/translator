from telethon import TelegramClient, events
#id, hash from https://my.telegram.org/apps
api_id = ''
api_hash = ''

client = TelegramClient('anon', api_id, api_hash)
client.start()

# channel id of the channels from which messages are sent, forwarding bot
@client.on(events.NewMessage((-1001223955273, -1001641260594)))
async def main(event):
    await client.forward_messages(7402205329, event.message)

# client.run_until_disconnected()

#bot forward to final channel
@client.on(events.NewMessage(7402205329))
async def main(event):
    await client.forward_messages(-1002425747864, event.message)

client.run_until_disconnected()
