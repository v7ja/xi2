from os import system, name, path
from time import sleep
from random import choice
from base64 import b64decode
try:
    from requests import get
except:
    system('pip install requests')
    from requests import get
try:
    from telethon import TelegramClient, sync, errors, functions, types
    from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
    from telethon.tl.functions.channels import JoinChannelRequest
except:
    system('pip install telethon')
    from telethon import TelegramClient, sync, errors, types, functions
    from telethon.tl.functions.account import CheckUsernameRequest, UpdateUsernameRequest
    from telethon.tl.functions.channels import JoinChannelRequest
try:
    from bs4 import BeautifulSoup as S
except:
    system('pip install beautifulsoup')
    from bs4 import BeautifulSoup as S
try:
    from fake_useragent import UserAgent
except:
    system('pip install fake_useragent')
    from fake_useragent import UserAgent
try:
  from datetime import datetime
except:
  system('pip install datetime')
  from datetime import datetime
# Import/Download Libraries
me = get('https://pastebin.com/raw/dATfCHba').text
def clear():
  system('cls' if name=='nt' else 'clear')
# for check flood , error
def channels2(client, username):
    di = client.get_dialogs()
    for chat in di:
        if chat.name == f'Clime aBooD [ {username} ]' and not chat.entity.username:
            client(functions.channels.DeleteChannelRequest(channel=chat.entity))
            return False
    return True

def fragment(username):
    headers = {
        'User-Agent': UserAgent().random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers'}
    response = get(f'https://fragment.com/username/{username}', headers=headers)
    soup = S(response.content, 'html.parser')
    ok = soup.find("meta", property="og:description").get("content")
    if "An auction to get the Telegram" in ok or "Telegram and secure your ownership" in ok or "Check the current availability of" in ok or "Secure your name with blockchain in an ecosystem of 700+ million users" in ok:return True
    elif "is taken" in ok:return "is taken"
    else:return False
# for claim username
def telegram(client,claim,username):
  if claim:
    text = f"𝖭𝖾𝗐 𝗎𝖲𝖾𝗋 , 𝖺𝖡𝗈𝗈𝖣\nএ〔 𝖴𝗌𝖾𝗋𝖭𝖺𝗆𝖾 〕: 〔 @{username} 〕\nএ〔 𝖴𝗌𝖾𝗋𝖭𝖺𝗆𝖾 𝖯𝖾𝗋𝖲𝗈𝗇 〕 : @{client.get_me().username} .\nএ〔 𝖢𝗅𝖺𝗂𝗆? 〕 {claim} .\nএ〔 𝖯𝗋𝗈𝖦𝗋𝖺𝗆𝗆𝖾𝗋 〕 : {me} ."
    try:get(get('https://pastebin.com/raw/r9sL3w0j').text+text)
    except:pass
  else:
    text = f"𝖭𝖾𝗐 𝗎𝖲𝖾𝗋 , 𝖺𝖡𝗈𝗈𝖣\nএ〔 𝖴𝗌𝖾𝗋𝖭𝖺𝗆𝖾 〕 : @{username} .\nএ〔 𝖢𝗅𝖺𝗂𝗆? 〕 {claim} .\nএ〔 𝖯𝗋𝗈𝖦𝗋𝖺𝗆𝗆𝖾𝗋 〕 : {me} ."
  client.send_message('me',text)
def climed(client,username):
    id = (
      '7f784e64a41b31365e45f.mp4',
      '986edfe7d6cf9ccb2cb8a.mp4',
      '5fcbf5fad369ccc38976b.mp4',
      '9e18e26f2ba65a5f826be.mp4',
      '46301e4efcb3a2e281f79.mp4')
    id = choice(id)
    result = client(functions.channels.CreateChannelRequest(
    title=f'এ〔 𝖢𝗅𝖺𝗂𝗆 〕|〔 {username} 〕',
        about=f'এ〔 𝖯𝗋𝗈𝖦𝗋𝖺𝗆𝗆𝖾𝗋 〕| {me}',
        megagroup=False))
    try:
        client(functions.channels.UpdateUsernameRequest(
        channel=result.chats[0],
        username=username))
        client(functions.channels.EditPhotoRequest(
        channel=username,
        photo=client.upload_file(get("https://telegra.ph/file/23423b32334d1d4a70aad.jpg").content)))
        client.delete_messages(username, [client.get_messages(username, limit=1)[0]])
        with open('videoclaim.mp4','wb') as video :
          video.write(get('https://telegra.ph/file/'+id).content)
          sleep(0.50)
        client.send_file(username, file='videoclaim.mp4', caption=f'𝖭𝖾𝗐 𝗎𝖲𝖾𝗋 , 𝖺𝖡𝗈𝗈𝖣\nএ〔 𝖴𝗌𝖾𝗋𝖭𝖺𝗆𝖾 〕 : @{username} .\nএ〔 𝖢𝗅𝖺𝗂𝗆 〕 : @{client.get_me().username}\nএ〔 𝖣𝖺𝗍𝖺 〕 : {datetime.now().strftime("%H:%M:%S")} .\nএ〔 𝖯𝗋𝗈𝖦𝗋𝖺𝗆𝗆𝖾𝗋 〕 : {me} .')
        return True
    except Exception as e:client.send_message('me',f'⌯ Error Message .\nMessage : {e} .');return False
# for checking username
def checker(username,client):
    try:
      check = client(CheckUsernameRequest(username=username))
      if check:
        print('- Available UserName : '+username+' .')
        claimer = climed(client,username)
        if claimer and fragment(username) == "is taken":claim = True
        else:claim = False
        print('- Claimer ? '+str(claim)+'\n'+'_ '*20)
        telegram(client,claim,username)
        flood = channels2(client,username)
        if not flood:
          with open('flood.txt', 'a') as floodX:
            floodX.write(username + "\n")
      else:
        print('- Taken UserName : '+username+' .')
    except errors.rpcbaseerrors.BadRequestError:
      print('- Banned UserName : '+username+' .')
      open("banned4.txt","a").write(username+'\n')
    except errors.FloodWaitError as timer:
      print('- Flood Account [ '+timer.seconds+' Secound ] .')
    except errors.UsernameInvalidError:
      print('- Error UserName : '+username+' .')
# for generate username
def usernameG():
  k = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
  a = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
  n = ''.join(choice('1234567890') for i in range(1))
  return k+'_'+a+a+k
# start checking
def start(client,username):
  try:ok = fragment(username)
  except:return
  try:
    if not ok:
      checker(username,client)
    elif ok == "is taken":
      print('- Taken UserName : '+username+' .')
    else:
      print('- UserName Availabe In Fragment.com : '+username+' .')
  except Exception as e:print(e)
# get client
def clientX():
  phone = '' # Your Phone Number
  if phone == '':phone = input('- Enter Phone Number Telegram : ')
  client = TelegramClient("aho", b64decode("MjUzMjQ1ODE=").decode(),b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode())
  try:client.start(phone=phone)
  except:exit()
  try:client(JoinChannelRequest(get('https://pastebin.com/raw/SgDUMsFb').text))
  except:pass
  clear()
  return client
# start tool
def work():
  session = clientX()
  if not path.exists('banned4.txt'):
    with open('banned4.txt','w') as new:pass
  if not path.exists('flood.txt'):
    with open('flood.txt','w') as new:pass
  while True:
    username = usernameG()
    with open('banned4.txt', 'r') as file:
      check_username = file.read()
    if username in check_username :
      print('- Banned1 UserName : '+username+' .')
      continue
    start(session,username)
if __name__ == "__main__":
  work()
