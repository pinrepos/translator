from telethon import TelegramClient, events

api_id = '23262703'
api_hash = 'afe205bb6157095277ffcc8ee2313511'

client = TelegramClient('anon', api_id, api_hash)
client.start()


@client.on(events.NewMessage((-1001223955273, -1001641260594)))
async def main(event):
    await client.forward_messages(7402205329, event.message)

# client.run_until_disconnected()


@client.on(events.NewMessage(7402205329))
async def main(event):
    await client.forward_messages(-1002425747864, event.message)

client.run_until_disconnected()
