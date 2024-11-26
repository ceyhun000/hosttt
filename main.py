from telethon import TelegramClient, events , functions,types,Button,errors
from telethon.tl.types import ChannelParticipantsAdmins,ChannelParticipantsSearch,Chat, Channel,ChatPhoto,ChatBannedRights
from telethon.tl.functions.messages import EditMessageRequest
from telethon.tl.functions.channels import GetFullChannelRequest,EditAdminRequest,GetParticipantsRequest,EditBannedRequest
from telethon.tl.types import Channel, Chat, ChannelParticipant,ChatAdminRights,PeerChannel,ChannelParticipantsKicked,ChannelParticipantsBanned,UserStatusOnline
from datetime import datetime
from telethon.tl.types import (
    UserStatusOnline,
    UserStatusOffline,
    UserStatusRecently,
    UserStatusLastWeek,
    UserStatusLastMonth
)
from googletrans import Translator
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
from art import text2art
from PIL import Image
from pydub import AudioSegment
from pydub.utils import which
from bs4 import BeautifulSoup
from random import choice, randint
import asyncio
import time
import re
import json
import os
import math
import requests
import random
import psutil
import pytz

telethon_api_id = "28582331"
telethon_api_hash = "99c9b25ffdbc9e8c0a698eb187f7f131"

client = TelegramClient("telethon_session", telethon_api_id,telethon_api_hash)

OWNER_ID = 7311719460

def is_owner(event):
    return event.sender_id == OWNER_ID

# comlist komutu
@client.on(events.NewMessage(pattern=r'\.komutlar'))
async def comlist(event):
    if not is_owner(event):
        return
    commands = """
    ```
**🛠 Telethon Listi:**
1. 🟢 **.alive** - bot aktiv komutu 
2. ℹ️ **.infoqrup** - qrup haqqında informasiya 
3. 👑 **.uspromote** - useri admin etmək
6. ⚠️ **.usdemote** - userin adminliyini almaq
8. 📇 **.addkk** - kontakta əlavə etmək (istifadə: reply + .addkk ad)
9. 🗑 **.allkkdel** - toplu kontakt silmək
10. 🎨 **.asc <mətin>** - sözləri ascii fonta çevirmək 
12. 🌐 **.lang <mətin>** - cümlə və sözləri tərcümə etmək
13. 🇬🇧 **.langEng <mətin>** - cümlə və sözləri ingilis dilinə çevirmək
14. 📈 **.curren** - valyuta çevirici
15. π **.riyaz** - riyaziyyat misalları həll etmək
17. 🎵 **.liriks** - mahnı sözləri tapmaq
18. 📜 **.adminl** - qrupun admin listi
19. 👥 **.tektag** - tək-tək tag etmək
20. 🛑 **.stoptag** - tag etməni dayandır
22. 📞 **.kk (say) [isim]** - avtoamtik random kontakta əlavə etmək
24. ❌ **.allban** - avtomatik bütün istifadəçiləri ban etmək
25. 🔁 **.sback** - sözləri tərs çevirmək
26. 🖼 **.profilkolaj** - profilləri birləşdirmə
26. ⛔️ **.bansayi** - qrupdakı ban və fban sayı
30. ☁️ **.sbuludu** - sözlərdən şəkil düzəltmək
33. ⏱ **.songorulme** - istifadəçinin son görülmə vaxtını göstərir
34. 🎧 **.sesler** - Səs effektləri listini göstərir
35. 📥 **.add [səs adı]** - səsə reply ataraq səs listinə əlavə et
36. 😁 **$[ses adı]** - Ses listinden bir sesi $ bu işarə ilə göndər
37. 🧬 **.klon** - profilleri klonla
38. ↩️ **.back** - öz profilinə qayıt
39. 🎮 **.21** - 21 oyunu başladır `İstifadə: .21 [oyunçuların tağı]`
40. 🛑 **.bitir** - 21 oyununu dayandırır
41. 🎰 **.slot** - slot çarxı başladır
42. 💣 **.ride** - basqın komutu istifadə: .ride [söz]
43. ⏹ **.stopride** - basqını dayandır
44. 🕕 **.tname** - ada saat əlavə et
45. 💬 **.pm** - şəxsi mesaj göndərmə
46. 🧹 **.delpm** - şəxsi mesajları toplu silmə
47. ⏰ **.reminder <zaman> <mesaj>** - xatırlatma
48. ⏳ **.timer** - zaman sayacı (saat:dəqiqə:saniyə)
49. 🌟 **.emtag** - emoji ilə tağ prosesi
50. 🛑 **.tagstop** - emoji ilə tağ prosesini dayandır
51. 🔄 **.reset** - qrup sıfırlamaq
52. 🖥 **.pros** - cihaz prosessoru
53. 🔤 **.setname** - ilk adı oto dəyişmə
54. 🆕 **.setusername** - etiketi oto dəyişmə
55. 👑 **.admin** - saxta adminlik vermə
56. 🦊 **.fake** - random eylem atmaq
```
    """
    await event.reply(commands)

# aktiv komutu

@client.on(events.NewMessage(pattern=r'\.alive'))
async def active_command(event):
    cool_text = "𐂡 卄ㄖ丂ㄒ𓅆"
    await event.edit(f"⚝ {cool_text} `userbot aktivdir...`")

# qrup info

@client.on(events.NewMessage(pattern=r'\.infoqrup'))
async def handler(event):
    if not is_owner(event):
        return
    chat = await event.get_chat()

    if isinstance(chat, (Channel, Chat)):
        try:
            full_chat = await client(GetFullChannelRequest(channel=chat))

            group_title = chat.title
            group_username = f"@{chat.username}" if chat.username else "None"
            group_id = chat.id
            members_count = full_chat.full_chat.participants_count

            # En eski mesajı al
            messages = await client.get_messages(chat.id, limit=1, reverse=True)
            if messages:
                oldest_message = messages[0]
                created_date = oldest_message.date.strftime('%Y-%m-%d %H:%M:%S')
            else:
                created_date = "Unknown"

            bots_count = 0
            admins_count = 0
            creator = None

            async for participant in client.iter_participants(chat.id):
                if participant.bot:
                    bots_count += 1
                elif isinstance(participant, ChannelParticipant):
                    if participant.admin_rights and participant.admin_rights.is_creator:
                        creator = participant
                    if participant.admin_rights and participant.admin_rights.is_admin:
                        admins_count += 1

            if creator:
                creator_name = creator.user.first_name
                creator_username = f"@{creator.user.username}" if creator.user.username else "None"
                creator_info = f"[{creator_name}](tg://user?id={creator.user.id}) ({creator_username})"
            else:
                creator_info = "Unknown"

            group_details = (
                f"**Group Information**\n"
                f"Initial Name: {group_title}\n"
                f"Tag: {group_username}\n"
                f"Group ID: {group_id}\n"
                f"Group Creation Date: {created_date}\n"
                f"Member Count: {members_count}\n"
                f"Bot Count: {bots_count}\n"
                f"Admin Count: {admins_count}\n"
            )

            await event.reply(group_details)
        except Exception as e:
            await event.reply(f"Failed to retrieve group info. Error: {str(e)}")
    else:
        await event.reply("This command can only be used in groups or supergroups.")

# istifadəçi yetkiləndirmə və ya alma


admin_rights = ChatAdminRights(
    delete_messages=True,
    manage_call=True,  
    invite_users=True,
    change_info=False,
    ban_users=False,
    pin_messages=False,
    add_admins=False
)

no_rights = ChatAdminRights(
    delete_messages=False,
    manage_call=False,
    invite_users=False,
    change_info=False,
    ban_users=False,
    pin_messages=False,
    add_admins=False
)

@client.on(events.NewMessage(pattern=r'\.uspromote'))
async def promote_user(event):
    if not is_owner(event):
        return
    if not event.is_group:
        await event.reply("**Bu komutu sadece qruplarda istifadə edə bilərsiniz**")
        return

    user = None
    custom_title = ""

    if event.is_reply:
        reply_message = await event.get_reply_message()
        user = await client.get_entity(reply_message.from_id)
        custom_title = event.message.text.split(' ', 1)[1] if len(event.message.text.split(' ', 1)) > 1 else ""
    else:
        try:
            user_data = event.message.text.split(' ', 2)
            user = await client.get_entity(user_data[1])
            custom_title = user_data[2] if len(user_data) > 2 else ""
        except (IndexError, ValueError):
            await event.reply("**Zəhmət olmasa keçərli bir istifadəçi ID'si, etiket və ya mesaja cavab olaraq istifadə edin**")
            return

    if not user:
        await event.reply("**İstifadəçi tapılmadı**")
        return

    permissions = await client.get_permissions(event.chat_id, 'me')
    if permissions.is_admin:
        await client(EditAdminRequest(
            channel=PeerChannel(event.chat_id),
            user_id=user.id,
            admin_rights=admin_rights,
            rank=custom_title
        ))
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        await event.reply(f"**İstifadəçi {mention} indi admindir**")
    else:
        await event.reply("**Sizin bu qrupda istifadəçini admin etmə icazəniz yoxdur**")

@client.on(events.NewMessage(pattern=r'\.usdemote'))
async def demote_user(event):
    if not is_owner(event):
        return
    if not event.is_group:
        await event.reply("**Bu komutu sadece qruplarda istifadə edə bilərsiniz**")
        return

    user = None
    if event.is_reply:
        reply_message = await event.get_reply_message()
        user = await client.get_entity(reply_message.from_id)
    else:
        try:
            user = await client.get_entity(event.message.text.split()[1])
        except (IndexError, ValueError):
            await event.reply("**Zəhmət olmasa keçərli bir istifadəçi ID'si, etiket və ya mesaja cavab olaraq istifadə edin**")
            return

    if not user:
        await event.reply("**İstifadəçi tapılmadı**")
        return

    permissions = await client.get_permissions(event.chat_id, 'me')
    if permissions.is_admin:
        await client(EditAdminRequest(
            channel=PeerChannel(event.chat_id),
            user_id=user.id,
            admin_rights=no_rights,
            rank=""  # Kullanıcının yönetici olarak atanmadığını göstermek için boş bırakıyoruz
        ))
        mention = f"[{user.first_name}](tg://user?id={user.id})"
        await event.reply(f"**İstifadəçi {mention} artıq admin deyil**")
    else:
        await event.reply("**Sizin bu qrupda istifadəçini adminlikdən çıxarma icazəniz yoxdur**")

# tek kontakta salma

@client.on(events.NewMessage(pattern=r'\.addkk'))
async def setcc(event):
    # Eğer komut bir reply ise
    if event.is_reply:
        reply_message = await event.get_reply_message()
        user = await client.get_entity(reply_message.from_id)
        
        command_parts = event.message.text.split(' ', 1)
        if len(command_parts) > 1:
            new_name = command_parts[1]
        else:
            new_name = user.first_name
        
        try:
            await client(functions.contacts.AddContactRequest(
                id=user.id,
                first_name=new_name,
                last_name='',
                phone=''
            ))
            await event.edit(f"**{user.first_name} artıq kontaktdır və adı {new_name} olaraq dəyişdirildi**")
        except Exception as e:
            await event.edit(f"**Xəta baş verdi:** {str(e)}")
    
    else:
        command_parts = event.message.text.split(' ', 2)
        if len(command_parts) < 3:
            await event.edit("**Kullanıcı ID/etiket və yeni ad daxil edilməlidir**")
            return
        
        identifier = command_parts[1]
        new_name = command_parts[2]
        
        try:
            user = await client.get_entity(identifier)
            await client(functions.contacts.AddContactRequest(
                id=user.id,
                first_name=new_name,
                last_name='',
                phone=''
            ))
            await event.edit(f"**{user.first_name} artıq kontaktdır və adı {new_name} olaraq dəyişdirildi**")
        except Exception as e:
            await event.edit(f"**Xəta baş verdi:** {str(e)}")

# toplu kontakt silme

@client.on(events.NewMessage(pattern=r'\.allkkdel'))
async def delkontaktall(event):
    try:
        contacts = await client(functions.contacts.GetContactsRequest(hash=0))
        if not contacts.users:
            await event.edit("**Heç bir kontakt tapılmadı**")
            return
        
        for user in contacts.users:
            try:
                await client(functions.contacts.DeleteContactsRequest(id=[user.id]))
                await event.edit(f"**{user.first_name} adlı istifadəçi silindi**")
                time.sleep(2)  
            except Exception as e:
                if "A wait of" in str(e):
                    wait_time = int(''.join(filter(str.isdigit, str(e))))
                    await event.edit(f"**Silmə limitinə çatıldı \n{wait_time} saniyə gözləmə**")
                    time.sleep(wait_time)
                else:
                    await event.edit(f"**{user.first_name} adlı istifadəçi silinərkən xəta baş verdi:** {str(e)}")
                    continue
        
        await event.edit("**Bütün kontaktlar silindi**")
    except Exception as e:
        await event.edit(f"**Xəta baş verdi:** {str(e)}")

# yazını ascii etmək

@client.on(events.NewMessage(pattern=r'\.asc (.+)'))
async def ascii(event):
    if event.is_reply:
        replied_message = await event.get.reply_message()
        text = replied_message.message
    else:
        text = event.pattern_match.group(1)

    ascii_art = text2art(text)

    await event.edit(f"```\n{ascii_art}\n```", parse_mode = 'markdown')

# bütün dilləri azərbaycan dilinə çevirmə

translator = Translator()

@client.on(events.NewMessage(pattern=r'\.lang( .+|$)'))
async def translate_text(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
        text_to_translate = reply_message.text
    else:
        if len(event.message.text.split()) < 2:
            await event.reply("Usage: .translate <text> or reply to a message with .translate")
            return
        text_to_translate = event.message.text.split(maxsplit=1)[1]
    
    try:
        translated = translator.translate(text_to_translate, dest='az')
        translated_text = translated.text

        await event.reply(f"✅ 𝚃𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚒𝚘𝚗 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎\n\n`Original word`: **{text_to_translate}**\n`Translated word`: **{translated_text}**")
    
    except Exception as e:
        await event.reply(f"An error occurred: {str(e)}")

# bütün dilləri İngilis dilinə çevirmə

@client.on(events.NewMessage(pattern=r'\.langEng( .+|$)'))
async def translate_text_eng(event):
    if event.is_reply:
        reply_message = await event.get_reply_message()
        text_to_translate = reply_message.text
    else:
        if len(event.message.text.split()) < 2:
            await event.reply("Usage: .translateEng <text> or reply to a message with .translateEng")
            return
        text_to_translate = event.message.text.split(maxsplit=1)[1]

    try:
        translated = translator.translate(text_to_translate, dest='en')
        translated_text = translated.text

        await event.reply(f"✅ 𝚃𝚛𝚊𝚗𝚜𝚕𝚊𝚝𝚒𝚘𝚗 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎\n\n`Original word`: **{text_to_translate}**\n`Translated word`: **{translated_text}**")
    
    except Exception as e:
        await event.reply(f"An error occurred: {str(e)}")


# riyaziyyat hell etme kodlari

@client.on(events.NewMessage(pattern=r'\.riyaz( .+|$)'))
async def calculate_expression(event):
    try:
        if event.is_reply:
            reply_message = await event.get_reply_message()
            expression = reply_message.text
        else:
            args = event.message.text.split(maxsplit=1)
            if len(args) < 2:
                await event.reply("Usage: .cal <expression> or reply to a message with .cal")
                return
            expression = args[1]

        expression = expression.replace("√", "math.sqrt")

        result = eval(expression, {"__builtins__": None}, {"math": math})

        await event.reply(f"Cavab:\n{result}")

    except Exception as e:
        await event.reply(f"XƏTA: {str(e)}")

# valyuta ceviren

def stylize_text(text):
    return f"✨ **{text}** ✨"

@client.on(events.NewMessage(pattern=r'\.curren'))
async def currency(event):
    try:
        text = event.message.text.split(" ", 1)
        if len(text) < 2:
            await event.reply(stylize_text("Düzgün format: `.valyuta məbləğ FROM TO` (məsələn, `.valyuta 100 USD EUR`)"))
            return
        
        amount, from_currency, to_currency = text[1].split(" ")
        amount = float(amount)
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url).json()

        if response.get("error"):
            await event.reply(stylize_text(f"Xəta: {response['error']}"))
            return

        if to_currency not in response['rates']:
            await event.reply(stylize_text(f"Dəyişmə dərəcəsi tapılmadı: {to_currency}"))
            return

        rate = response['rates'][to_currency]
        converted_amount = amount * rate
        
        await event.reply(stylize_text(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"))

    except ValueError:
        await event.reply(stylize_text("Yanlış məbləğ. Zəhmət olmasa düzgün məbləğ daxil edin."))
    except IndexError:
        await event.reply(stylize_text("Düzgün format: `.valyuta məbləğ FROM TO` (məsələn, `.valyuta 100 USD EUR`)"))
    except Exception as e:
        await event.reply(stylize_text(f"Xəta baş verdi: {str(e)}"))

# mahni sozu tapma

GENIUS_API = "FdiG8NMlpEVOW3fJnaJqW7Vom-8p9lUauP_jNuA5PLbX3L-kDznZlIghV2Opiooz"

def get_lyrics(song_title):
    headers = {
        'Authorization': f'Bearer {GENIUS_API}'
    }
    search_url = 'https://api.genius.com/search'
    params = {
        'q': song_title
    }
    
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()
   
    try:
        song_path = data['response']['hits'][0]['result']['path']
        lyrics_url = f'https://genius.com{song_path}'
       
        lyrics_response = requests.get(lyrics_url)
        soup = BeautifulSoup(lyrics_response.text, 'html.parser')
      
        lyrics_div = soup.find('div', class_='lyrics')
        if lyrics_div:
            lyrics = lyrics_div.get_text(strip=True, separator="\n")
        else:
            lyrics_div = soup.find('div', class_=re.compile('Lyrics__Container'))
            if lyrics_div:
                lyrics = lyrics_div.get_text(strip=True, separator="\n")
            else:
                lyrics = "Mahnı sözləri tapılmadı."

        return f"🅒🅞🅛🅓 🅤🅢🅔🅡🅑🅞🅣\n\n{lyrics}"
        
    except IndexError:
        return "Mahnı sözləri tapılmadı."
    except Exception as e:
        return f"Xəta baş verdi: {str(e)}"

@client.on(events.NewMessage(pattern=r'\.liriks (.+)'))
async def lyrics(event):
    song_title = event.pattern_match.group(1)
    lyrics_text = get_lyrics(song_title)
    
    await event.reply(lyrics_text)

# admin listi

@client.on(events.NewMessage(pattern=r'\.adminl', outgoing=True))
async def adminlist_command(event):
    chat = await event.get_input_chat()
    admins = await client(GetParticipantsRequest(
        channel=chat,
        filter=ChannelParticipantsAdmins(),
        offset=0,
        limit=100,
        hash=0
    ))

    admin_list = []
    for admin in admins.participants:
        user = await client.get_entity(admin.user_id)
        custom_title = admin.rank if admin.rank else "No Title"
        admin_info = f"➤ [{user.first_name}](tg://user?id={user.id}): [{custom_title}]"
        admin_list.append(admin_info)

    if admin_list:
        admin_info_message = "**Qrupdakı Adminlər:**\n\n" + "\n".join(admin_list)
        admin_info_message += f"\n\n🜲 **Admin Sayı:** {len(admin_list)}"
    else:
        admin_info_message = "🚫 Bu qrupda admin yoxdur."

    await event.respond(admin_info_message, link_preview=False)

# etiketleme 

stop_labeling = False
labeling_task = None

async def label_users(event, label_text):
    global stop_labeling, labeling_task
    chat = await event.get_input_chat()
    
    participants = await client(GetParticipantsRequest(
        channel=chat,
        filter=ChannelParticipantsSearch(''),
        offset=0,
        limit=200,
        hash=0
    ))

    user_list = [p for p in participants.users if not p.bot]
    total_users = len(user_list)

    if total_users == 0:
        await event.reply("Bu qrupda heç bir iştirakçı yoxdur.")
        return

    random.shuffle(user_list)
    count = 0

    for user in user_list:
        if count >= 100 or stop_labeling:
            break

        if user.username:
            mention = f"@{user.username}"
        else:
            mention = f"[{user.first_name}](tg://user?id={user.id})"
        
        message = f"{label_text} {mention}"

        try:
            await event.respond(message, link_preview=False)
            count += 1
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Xəta baş verdi: {str(e)}")

    if count == 0:
        await event.respond("Heç bir istifadəçi etiketlenmədi.")

@client.on(events.NewMessage(pattern=r'\.tektag', outgoing=True))
async def label_command(event): 
    await event.edit("**𐂡 卄ㄖ丂ㄒ𓅆 `userbot aktivləşdi...` \nEtiketləmə başladılır**")
    global stop_labeling, labeling_task
    if labeling_task and not stop_labeling:
        await event.edit("Etiketleme artıq davam edir.")
        return

    if stop_labeling:
        stop_labeling = False  

    text = event.text.split(" ", 1)
    if len(text) < 2:
        await event.reply("Düzgün format: .label <mesaj>")
        return

    label_text = text[1]
    labeling_task = asyncio.create_task(label_users(event, label_text))

@client.on(events.NewMessage(pattern=r'\.stoptag', outgoing=True))
async def lstop_command(event):
    global stop_labeling, labeling_task
    if not stop_labeling:
        stop_labeling = True
        if labeling_task:
            labeling_task.cancel()
            labeling_task = None
        await event.edit("**Etiketləmə dayandırıldı**")
    else:
        await event.edit("Etiketləmə zatən dayandırılıb")

# random kontakta elave elemek

@client.on(events.NewMessage(pattern=r'\.kk (\d+) (.+)'))
async def handle_kontakt(event):
    try:
        count = int(event.pattern_match.group(1))
        name = event.pattern_match.group(2)

        chat = await event.get_chat()
        
        participants = await client.get_participants(chat)
        
        eligible_users = [p for p in participants if p.bot == False and not p.deleted]

        if len(eligible_users) < count:
            await event.reply(f"**Qrupta yetəri qədər istifadəçi mövcud deyil. Sadəcə {len(eligible_users)} istifadəçilər əlavə olunabilər**")
            return

        
        selected_users = random.sample(eligible_users, count)
        
        for user in selected_users:
            try:
                await client(functions.contacts.AddContactRequest(
                    id=user.id,
                    first_name=name,
                    last_name='',
                    phone='',
                    add_phone_privacy_exception=False
                ))
                await asyncio.sleep(1)  # İşlem yoğunluğunu azaltmak için kısa bir bekleme
            except Exception as e:
                print(f"Bir hata oluştu: {e}")

        await event.reply(f'{len(selected_users)} **İstifadəçilər uğurla kontakta əlavə olundu və {name} ilə dəyişdirildi 🎉**')

    except Exception as e:
        await event.reply(f'Xəta: {e}')

# qrup sifirla

@client.on(events.NewMessage(pattern="^.allban$", outgoing=True))
async def banall(event):
    await event.delete()
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.edit("Bu əmri icra etmək üçün admin olmalısınız.")
        return

    me = await event.client.get_me()
    all_participants = await event.client.get_participants(event.chat_id)
    for user in all_participants:
        if user.id == me.id:
            continue
        try:
            await event.client(EditBannedRequest(
                event.chat_id, user.id, ChatBannedRights(
                    until_date=None,
                    view_messages=True
                )
            ))
            await asyncio.sleep(0.5)
        except Exception as e:
            await asyncio.sleep(0.3)

    await event.edit("**Boss girdi çıxdı😈**\n Qrup sıfırlandı")

# sozu terse cevir

@client.on(events.NewMessage(pattern= r'\.sback\s*(.*)'))
async def reverse_words(event):
    try:
        message = event.pattern_match.group(1)
        if event.is_reply and not message:
            reply_message = await event.get_reply_message()
            message = reply_message.message

        if message:
            ters_metn = ' '.join([kelme[::-1] for kelme in message.split()[::-1]])
            await event.edit(f"🔄 **Çevrilmiş cümlə:** {ters_metn}")
        else:
            await event.edit("🚫 **mətn daxil edilməyib**")
    
    except Exception as e:
        await event.reply(f"**Xeta:** {str(e)}")

# profil kolaj

@client.on(events.NewMessage(pattern=r'\.profilkolaj\s+(@\w+(?:\s+@\w+)*)'))
async def profile_pic_collage(event):
    try:

        usernames = event.pattern_match.group(1).split()

        if not os.path.exists("profile_pics"):
            os.makedirs("profile_pics")

        profile_pics = []
        for username in usernames:
            user = await client.get_entity(username)
            if user.photo:
                photos = await client(functions.photos.GetUserPhotosRequest(
                    user_id = user.id,
                    offset = 0,
                    max_id = 0,
                    limit = 1
                ))
                if photos.photos:
                    photo = photos.photos[0]
                    file = await client.download_media(photo, file="profile_pics/")
                    profile_pics.append(file)

        images = [Image.open(pic) for pic in profile_pics]
        widths,heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        max_height = max(heights)

        collage = Image.new('RGB', (total_width,max_height))

        x_offset = 0
        for img in images:
            collage.paste(img, (x_offset,0))
            x_offset += img.width

        collage_file = "collage.jpg"
        collage.save(collage_file)
        
        await client.send_file(event.chat_id, collage_file, caption = "**Istifadəçilərin profilləri birləşdirildi**")
        
        for pic in profile_pics:
            os.remove(pic)
        os.remove(collage_file)

    except Exception as e:
        await event.reply(f"Xeta: {str(e)}")

# stats komutu 

@client.on(events.NewMessage(pattern=r'\.bansayi'))
async def allbanuser(event):
    try:
        # Qrup ID'sini alın
        chat = await event.get_input_chat()

        banned_users = await client.get_participants(chat, filter=ChannelParticipantsKicked)
        total_bans = len(banned_users)

        fban_users = await client.get_participants(chat, filter=ChannelParticipantsBanned)
        total_fbans = len(fban_users)

        stats_message = (
            f"🚫 **Banlı istifadəçilər:** `{total_bans}`\n"
            f"🔨 **Fbanlı istifadəçilər:** `{total_fbans}`"
        )
        await event.reply(stats_message)

    except Exception as e:
        await event.reply(f"🚫 Xəta baş verdi: {str(e)}")

# cihaz prosessor yoxlanisi

@client.on(events.NewMessage(pattern=r'\.prosessor'))
async def processor(event):
    try:

        await event.delete()

        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq().current

        report = (
            f"🖥 **Processor report**:\n\n"
            f"🔍 **Usage Percentage:** `{cpu_percent}%`\n"
            f"⚙️ **Number of Cores:** `{cpu_count}`\n"
            f"📊 **Frequency:** `{cpu_freq} MHZ`\n"
        )

        await event.reply(report)

    except Exception as e:
        await event.reply(f"🚫 Xəta baş verdi: {str(e)}")

# istifadəci informasiyasi

user_data = {}

# Kullanıcı verilerini JSON dosyasına kaydetmek için fonksiyon
def save_user_data():
    with open("user_data.json", "w") as f:
        json.dump(user_data, f, indent=4)

# Kullanıcı verilerini yüklemek için fonksiyon
def load_user_data():
    global user_data
    try:
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = {}

load_user_data()

# .usinfo komutu ile kullanıcının bilgilerini gösteren fonksiyon
@client.on(events.NewMessage(pattern=r"\.info"))
async def user_info(event):
    user = None
    message = event.message

    if message.is_reply:
        user = await message.get_reply_message()
        user = user.sender
    else:
        args = event.message.text.split()
        if len(args) < 2:
            await event.reply("İstifadə: .usinfo <istifadəçi_id | istifadəçi_tag> və ya bir istifadəçi mesajına cavab verərək .usinfo yazın")
            return

        identifier = args[1]

        try:
            if identifier.isdigit():
                user = await client.get_entity(int(identifier))
            else:
                user = await client.get_entity(identifier)
        except Exception as e:
            await event.reply(f"Xəta baş verdi: {str(e)}")
            return

    if user:
        user_id = str(user.id)
        first_name = user.first_name

        if user_id not in user_data:
            user_data[user_id] = {"first_names": []}

        if first_name not in user_data[user_id]["first_names"]:
            user_data[user_id]["first_names"].append(first_name)
            save_user_data()

        first_names_list = '\n'.join(user_data[user_id]["first_names"])

        user_details = (
            f"**İstifadəçi Məlumatı**\n"
            f"ID: {user.id}\n"
            f"Adı: {user.first_name}\n"
            f"Soyadı: {user.last_name}\n"
            f"İstifadəçi Adı: @{user.username}\n"
            f"Telefon Nömrəsi: {user.phone}\n"
            f"Botdur: {user.bot}\n"
            f"Dil Kodu: {user.lang_code}\n"
            f"\n**İstifadə etdiyi Adlar:**\n{first_names_list}"
        )
        await event.reply(user_details)
    else:
        await event.reply("İstifadəçi tapılmadı.")

@client.on(events.NewMessage())
async def track_first_names(event):
    user = event.sender
    if user:
        user_id = str(user.id)
        first_name = user.first_name

        if user_id not in user_data:
            user_data[user_id] = {"first_names": []}

        if first_name not in user_data[user_id]["first_names"]:
            user_data[user_id]["first_names"].append(first_name)
            save_user_data()

# fikir toplusu

brainstorm_ideas = {}

@client.on(events.NewMessage(pattern=r"\.ideya (.+)$"))
async def fikir(event):
    if not event.is_group:
        await event.reply("**Bu əmri yalnız qruplarda istifadə edə bilərsiniz**")
        return

    topic = event.pattern_match.group(1)
    chat_id = event.chat_id

    if chat_id not in brainstorm_ideas:
        brainstorm_ideas[chat_id] = {"topic": topic, "ideas": []}
        await event.reply(f"**'{topic}' mövzusunda beyin fırtınası başladı! Fikirlərinizi yazın:**")
    else:
        await event.reply(f"**Artıq '{brainstorm_ideas[chat_id]['topic']}' mövzusunda beyin fırtınası davam edir. Fikirlərinizi yazın:**")

@client.on(events.NewMessage)
async def collect_ideas(event):
    chat_id = event.chat_id

    if chat_id in brainstorm_ideas and event.message.text and not event.message.text.startswith('.'):
        idea = event.message.text
        brainstorm_ideas[chat_id]["ideas"].append(idea)

# movzu haqqinda fikirler

@client.on(events.NewMessage(pattern=r"\.ideyalar$"))
async def show_ideas(event):
    if not event.is_group:
        await event.reply("**Bu əmri yalnız qruplarda istifadə edə bilərsiniz**")
        return

    chat_id = event.chat_id

    if chat_id in brainstorm_ideas:
        ideas = brainstorm_ideas[chat_id]["ideas"]
        if ideas:
            ideas_text = "\n".join(f"- {idea}" for idea in ideas)
            await event.reply(f"**'{brainstorm_ideas[chat_id]['topic']}' mövzusunda toplanan fikirlər:**\n{ideas_text}")
        else:
            await event.reply("**Hələ heç bir fikir toplanmayıb**")
    else:
        await event.reply("**Hazırda davam edən bir beyin fırtınası yoxdur**")

@client.on(events.NewMessage(pattern=r"\.stopideya$"))
async def end_brainstorm(event):
    if not event.is_group:
        await event.reply("**Bu əmri yalnız qruplarda istifadə edə bilərsiniz**")
        return

    chat_id = event.chat_id

    if chat_id in brainstorm_ideas:
        del brainstorm_ideas[chat_id]
        await event.reply("**Beyin fırtınası bitdi! Toplanan fikirlərə baxmaq üçün `.fikirlər` yazın**")
    else:
        await event.reply("**Bitirilecek bir beyin fırtınası yoxdur**")

@client.on(events.NewMessage(pattern=r'\.songorulme\s+(@\S+)'))
async def lastseen(event):
    try:
        username = event.pattern_match.group(1)
        user = await client.get_entity(username)

        # Azərbaycan saat zonası
        az_time_zone = pytz.timezone('Asia/Baku')

        if user.status:
            if isinstance(user.status, UserStatusOnline):
                await event.edit(f"**{username} indi online-dir**")
            elif isinstance(user.status, UserStatusOffline):
                # Tarixi Azərbaycan vaxtına çevir
                last_seen = user.status.was_online.astimezone(az_time_zone).strftime("%d-%m-%Y %H:%M:%S")
                await event.edit(f"**{username} sonuncu dəfə {last_seen} tarixində online olub**")
            elif isinstance(user.status, UserStatusRecently):
                await event.edit(f"**{username} son vaxtlar online olub**")
            elif isinstance(user.status, UserStatusLastWeek):
                await event.edit(f"**{username} keçən həftə online olub**")
            elif isinstance(user.status, UserStatusLastMonth):
                await event.edit(f"**{username} keçən ay online olub**")
            else:
                await event.edit(f"**{username} çox uzun müddətdir online deyil**")
        else:
            await event.edit(f"**{username}'in online vəziyyəti mövcud deyil**")

    except Exception as e:
        await event.edit(f"**Xeta: {str(e)}**")

SOUNDS_DIR = "sounds/"

# .sounds komutu
@client.on(events.NewMessage(pattern=r"\.sounds$"))
async def list_sounds(event):
    if not is_owner(event):
        return
    
    try:
        sound_files = os.listdir(SOUNDS_DIR)
        if not sound_files:
            await event.reply("**Heç bir səs faylı tapılmadı**")
            return
        
        sound_list = "\n".join(f"→ {os.path.splitext(file)[0]}" for file in sound_files)
        
        # Telegram'ın karakter sınırını aşmaması için uzunluğu kontrol edin
        max_message_length = 4096
        if len(sound_list) > max_message_length:
            sound_chunks = [sound_list[i:i + max_message_length] for i in range(0, len(sound_list), max_message_length)]
            await event.edit("**Mövcud səs faylları:**")
            for chunk in sound_chunks:
                await event.reply(chunk)
        else:
            await event.edit(f"**Mövcud səs faylları:**\n\n{sound_list}")

    except Exception as e:
        await event.reply(f"**Bir xəta baş verdi:** {str(e)}")

SOUNDS_DIR = "sounds/"

# $ komutu
@client.on(events.NewMessage(pattern=r"\$([^\s]+)$"))
async def send_sound(event):
    if not is_owner(event):
        return

    sound_name = event.pattern_match.group(1).strip()
    
    try:
        sound_file = os.path.join(SOUNDS_DIR, f"{sound_name}.mp3")
        
        if os.path.exists(sound_file):
            if event.is_reply:
                reply_msg = await event.get_reply_message()
                await client.send_file(event.chat_id, sound_file, caption=f"**𐂡 卄ㄖ丂ㄒ𓅆 𝘀𝗼𝘂𝗻𝗱 𝗲𝗳𝗳𝗲𝗰𝘁**", reply_to=reply_msg.id)
            else:
                await client.send_file(event.chat_id, sound_file, caption=f"**𐂡 卄ㄖ丂ㄒ𓅆 𝘀𝗼𝘂𝗻𝗱 𝗲𝗳𝗳𝗲𝗰𝘁**")
            
            # Komutu içeren mesajı sil
            await event.delete()
        else:
            await event.reply("**Göstərilən adla bir səs faylı tapılmadı**")

    except Exception as e:
        await event.reply(f"**Bir xəta baş verdi:** {str(e)}")


SOUNDS_DIR = "sounds/"

# .addsound komutu
@client.on(events.NewMessage(pattern=r"\.add\s+(\S+)$"))
async def add_sound(event):
    if not is_owner(event):
        return

    sound_name = event.pattern_match.group(1).strip()
    
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        
        if reply_msg.voice or reply_msg.audio:
            try:
                # Ses dosyasını indir
                file_path = await client.download_media(reply_msg, file=SOUNDS_DIR)
                
                # MP3 formatına dönüştür
                audio = AudioSegment.from_file(file_path)
                output_file = os.path.join(SOUNDS_DIR, f"{sound_name}.mp3")
                
                audio.export(output_file, format="mp3")
                
                await event.edit(f"**{sound_name}** 𝚜ə𝚜 𝚜𝚘𝚞𝚗𝚍 𝚏𝚊𝚢𝚕ı𝚗𝚊 ə𝚕𝚊𝚟ə 𝚎𝚍𝚒𝚕𝚍𝚒")
                
            except Exception as e:
                if "ffmpeg" in str(e).lower():
                    await event.reply("❌ Xəta baş verdi: FFmpeg ile ilgili bir problem oluştu.")
                else:
                    await event.reply(f"❌ Xəta baş verdi: {str(e)}")
        else:
            await event.reply("**Reply atdığınız mesaj bir səs mesajı deyil**")
    else:
        await event.reply("**Bu əmri bir səs mesajına reply edərək istifadə edin**")

# istifadeci informasiya

user_data = {}

# Kullanıcı verilerini JSON dosyasına kaydetmek için fonksiyon
def save_user_data():
    with open("user_data.json", "w") as f:
        json.dump(user_data, f, indent=4)

# Kullanıcı verilerini yüklemek için fonksiyon
def load_user_data():
    global user_data
    try:
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = {}

load_user_data()

# .usinfo komutu ile kullanıcının bilgilerini gösteren fonksiyon
@client.on(events.NewMessage(pattern=r"\.usinfo"))
async def user_info(event):
    if not is_owner(event):
        return
    user = None
    message = event.message

    if message.is_reply:
        user = await message.get_reply_message()
        user = user.sender
    else:
        args = event.message.text.split()
        if len(args) < 2:
            await event.edit("İstifadə: .usinfo <istifadəçi_id | istifadəçi_tag> və ya bir istifadəçi mesajına cavab verərək .usinfo yazın")
            return

        identifier = args[1]

        try:
            if identifier.isdigit():
                user = await client.get_entity(int(identifier))
            else:
                user = await client.get_entity(identifier)
        except Exception as e:
            await event.reply(f"Xəta baş verdi: {str(e)}")
            return

    if user:
        user_id = str(user.id)
        first_name = user.first_name

        if user_id not in user_data:
            user_data[user_id] = {"first_names": []}

        if first_name not in user_data[user_id]["first_names"]:
            user_data[user_id]["first_names"].append(first_name)
            save_user_data()

        first_names_list = '\n'.join(user_data[user_id]["first_names"])

        user_details = (
            f"ℹ️ 𝚄𝚜𝚎𝚛 𝙸𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗\n\n"
            f"`ID`: {user.id}\n"
            f"`Adı`: {user.first_name}\n"
            f"`Soyadı`: {user.last_name}\n"
            f"`İstifadəçi Adı`: @{user.username}\n"
            f"`Telefon Nömrəsi`: {user.phone}\n"
            f"`Botdur`: {user.bot}\n"
            f"`Dil Kodu`: {user.lang_code}\n\n"
            f"\n𝚃𝚑𝚎 𝙽𝚊𝚖𝚎𝚜 𝙷𝚎 𝚄𝚜𝚎𝚜:\n```{first_names_list}```"
        )
        await event.edit(user_details)
    else:
        await event.edit("İstifadəçi tapılmadı.")

@client.on(events.NewMessage())
async def track_first_names(event):
    user = event.sender
    if user:
        user_id = str(user.id)
        first_name = user.first_name

        if user_id not in user_data:
            user_data[user_id] = {"first_names": []}

        if first_name not in user_data[user_id]["first_names"]:
            user_data[user_id]["first_names"].append(first_name)
            save_user_data()

# klon komutu

original_profile = {}
original_photo_path = None

@client.on(events.NewMessage(pattern=r'^\.klon$', outgoing=True))
async def clone_profile(event):
    global original_photo_path
    reply = await event.get_reply_message()
    if not reply or not reply.sender_id:
        await event.edit("Zəhmət olmasa, bir istifadəçinin mesajına cavab verin.")
        return

    user_full = await client(GetFullUserRequest(reply.sender_id))
    user = user_full.users[0]
    if not user:
        await event.edit("`İstifadəçi tapılmadı`")
        return

    user_first_name = user.first_name or ""
    await event.edit(f"{user_first_name} `prifilini klonlayıram🙈...`")

    try:
        
        me_full = await client(GetFullUserRequest('me'))
        me = me_full.users[0]
        original_profile['first_name'] = me.first_name
        original_profile['last_name'] = me.last_name
        original_profile['bio'] = me_full.full_user.about if me_full.full_user.about else ''

      
        photos = await client.get_profile_photos('me')
        if photos:
            original_photo = photos[0]
            original_photo_path = await client.download_media(original_photo, file='original_photo.jpg')
        else:
            original_photo_path = None

        
        photos = await client.get_profile_photos(user)
        if photos:
            photo = photos[0]
            uploaded_photo_path = await client.download_media(photo, file='uploaded_photo.jpg')

            
            with open(uploaded_photo_path, 'rb') as f:
                uploaded_photo = await client.upload_file(f)
            await client(UploadProfilePhotoRequest(file=uploaded_photo))
        else:
            await event.edit("`Bu istifadəçinin profil şəkli yoxdur`")


        await client(UpdateProfileRequest(
            first_name=user.first_name,
            last_name=user.last_name,
            about=user_full.full_user.about if user_full.full_user.about else ''
        ))

        await event.reply("`Profil uğurla klonlandı`")
    except Exception as e:
        await event.edit(f"Bir xəta baş verdi: {str(e)}")
    
       

@client.on(events.NewMessage(pattern=r'^\.back$', outgoing=True))
async def revert_profile(event):
    if not original_profile:
        await event.edit("`Klonlanmış profil məlumatları tapılmadı`")
        return

    try:
        await event.edit("`Orijinal profilə geri dönülür...`")

        
        if original_photo_path and os.path.exists(original_photo_path):
            with open(original_photo_path, 'rb') as f:
                original_photo = await client.upload_file(f)
            await client(UploadProfilePhotoRequest(file=original_photo))
            os.remove(original_photo_path)


        await client(UpdateProfileRequest(
            first_name=original_profile['first_name'],
            last_name=original_profile['last_name'],
            about=original_profile['bio']
        ))

        await event.reply("`Profil uğurla geri yükləndi`")
    except Exception as e:
        await event.edit(f"Bir xəta baş verdi: {str(e)}")

# slot

@client.on(events.NewMessage(pattern = r'\.slot'))
async def slot_command(event):
    slots = ['1','2','3','4','5','6','7','8','9']

    message = await event.edit("🎰 `Slot avtomatı çevrilir...`")

    for i in range(5):
        anime_result = f"{random.choice(slots)} {random.choice(slots)} {random.choice(slots)}"
        await event.edit(f"🎰 `{anime_result}`")
        await asyncio.sleep(1)

    result = [random.choice(slots) for _ in range(3)]
    final_result = f"{result[0]} {result[1]} {result[2]}"

    if len(set(result)) == 1:
        final_message = f"💥 **QAZANDIN** - `{final_result}`"
    else:
        final_message = f"😞 UDUZDUN - `{final_result}`"

    await event.edit(f"🎰 **Slot tamamlandı**\n\n `Nəticə:{final_message}`")

# 21 oyunu


active_game = False
players = []
current_sum = 0
turn_index = 0

@client.on(events.NewMessage(pattern=r'\.21(?: (.+))?'))
async def start_game(event):
    if not is_owner(event):
        return
    global active_game, players, current_sum, turn_index
    if active_game:
        await event.edit("🚨 **Artıq davam edən bir oyun var!**")
        return

    if event.pattern_match.group(1):
        player_ids = event.pattern_match.group(1).split()
        players = []
        
        for player in player_ids:
            if player.startswith('@'):
                try:
                    user = await event.client.get_entity(player)
                    players.append(user)
                except:
                    await event.edit(f"❌ **İstifadəçi tapılmadı:** `{player}`")
                    return
            else:
                await event.edit("⚠️ **Zəhmət olmasa istifadəçiləri @ və ya id ilə qeyd edin.**")
                return

        if len(players) < 2:
            await event.edit("⚠️ **Oyun üçün ən az iki oyunçu olmalıdır.**")
            return
        
        active_game = True
        current_sum = 0
        turn_index = 0
        first_player = players[0]
        
        players_list = '\n'.join([f'@{player.username}' if player.username else f'[{player.first_name}](tg://user?id={player.id})' for player in players])
        await event.edit(f"🥳 **21 oyunu başladı!**\n\n 🎮 **Oyunçular:**\n{players_list}\n\n👤 **İlk növbədə olan oyunçu:**\n[{first_player.first_name}](tg://user?id={first_player.id})\n**Zəhmət olmasa 1-3 arası rəqəmini seç.**")
    else:
        await event.edit("⚠️ **Zəhmət olmasa oyunçu ID-lərini və ya istifadəçi adlarını daxil edin.**\nNümunə: `.21 @player1 @player2`")

@client.on(events.NewMessage(pattern=r'([1-3])'))
async def player_turn(event):
    global active_game, players, current_sum, turn_index

    if not active_game:
        return

    current_player = players[turn_index]

    if event.sender_id != current_player.id:
        await event.reply(f"⛔ **İndi sənin növbən deyil!** \n\n🕹 **Növbəti oyunçu:** [{current_player.first_name}](tg://user?id={current_player.id})")
        return

    chosen_number = int(event.pattern_match.group(1))
    current_sum += chosen_number

    if current_sum >= 21:
        await event.reply(f"💥 **[{current_player.first_name}](tg://user?id={current_player.id}) 21 dedi və oyunu uduzdu!**\n❌ **Oyun bitdi!**")
        active_game = False
        return

    turn_index = (turn_index + 1) % len(players)
    next_player = players[turn_index]

    await event.reply(f"🔢 **Cəmi xal:** `{current_sum}`\n\n🎮 **Növbəti oyunçu:** [{next_player.first_name}](tg://user?id={next_player.id}), zəhmət olmasa 1, 2 və ya 3 rəqəmini seç.")
    
@client.on(events.NewMessage(pattern=r'\.bitir'))
async def end_game(event):
    if not is_owner(event):
        return
    global active_game, players, current_sum, turn_index
    if active_game:
        active_game = False
        await event.edit("🛑 **Oyun dayandırıldı.**")
    else:
        await event.edit("⚠️ **Davam edən oyun yoxdur!**")

# adımıza saat elave etmek

# ilk once azerbaycan saatini secirik

AZ_TIMEZONE = pytz.timezone('Asia/Baku')

async def update_name(client):
    while True:
        current_time = datetime.now(AZ_TIMEZONE).strftime("%H:%M")

        me = await client.get_me()
        first_name = me.first_name

        if len(first_name) + len(current_time) <= 64:
            new_last_name = current_time
        else:
            # Aksi takdirde saat kısmını kısaltıyoruz
            new_last_name = current_time[:64 - len(first_name)]

        await client(functions.account.UpdateProfileRequest(
            first_name=first_name,
            last_name=new_last_name
        ))

        await asyncio.sleep(60)

@client.on(events.NewMessage(pattern=r"\.tname$"))
async def tname(event):
    await event.edit("`Adınıza saat əlavə olundu`")

    await update_name(client)

# basqin komutu

spam_tasks = []

@client.on(events.NewMessage(pattern=r"\.ride (.+)"))
async def ride(event):
    if not is_owner(event):
        return
    message_to_spam = event.pattern_match.group(1)
    task = asyncio.create_task(spam_messages(event, message_to_spam))
    spam_tasks.append(task)
    await event.delete()

async def spam_messages(event, message):
    for i in range(100):
        await event.respond(message)
        await asyncio.sleep(1)
        if spam_tasks and any(task.cancelled() for task in spam_tasks):
            break

@client.on(events.NewMessage(pattern=r"\.stopride$"))
async def stopride(event):
    if not is_owner(event):
        return
    global spam_tasks

    if spam_tasks:
        for task in spam_tasks:
            task.cancel()

        await event.edit("`Bütün spam əməliyyatları dayandırıldı!`")
        spam_tasks = []
    else:
        await event.edit("`Davam edən spam əməliyyatı yoxdur`")

# global səssizə alma komutu

slient_users = []

@client.on(events.NewMessage(pattern=r'\.gmute'))
async def add_target_user(event):
    if event.is_private:
        return

    if event.is_reply:
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id
    else:
        try:
            user_id = int(event.message.text.split()[1])
        except (IndexError, ValueError):
            await event.edit("**Zəhmət olmasa keçərli bir istifadəçi ID'si daxil edin və ya komandanı bir mesaja cavab olaraq istifadə edin**")
            return

    if user_id not in slient_users:
        slient_users.append(user_id)
        user = await client.get_entity(user_id)
        mention = f"[{user.first_name}](tg://user?id={user_id})"
        await event.edit(f"**İstifadəçi {mention} indi izlənilir və mesajları silinəcək**")
    else:
        await event.edit(f"**İstifadəçi artıq izlənilir**")

@client.on(events.NewMessage(pattern=r'\.ungmute'))
async def remove_target_user(event):
    if event.is_private:
        return

    if event.is_reply:
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id
    else:
        try:
            user_id = int(event.message.text.split()[1])
        except (IndexError, ValueError):
            await event.edit("**Zəhmət olmasa keçərli bir istifadəçi ID'si daxil edin və ya komandanı bir mesaja cavab olaraq istifadə edin**")
            return

    if user_id in slient_users:
        slient_users.remove(user_id)
        user = await client.get_entity(user_id)
        mention = f"[{user.first_name}](tg://user?id={user_id})"
        await event.edit(f"**İstifadəçi {mention} artıq izlənilmir və mesajları silinməyəcək**")
    else:
        await event.edit("**İstifadəçi izlənilmir**")

@client.on(events.NewMessage)
async def delete_target_messages(event):
    if event.sender_id in slient_users:
        if event.is_group or event.is_channel:
            permissions = await client.get_permissions(event.chat_id, 'me')
            if permissions.delete_messages:
                await event.delete()
                print(f"{event.chat_id} chatında {event.sender_id} istifadəçisinin mesajı silindi")

# emoji ile tag

emojiler = [
    "😀😎🎉🔥💫", "🚀🌟🎯💥✨", "🎵🎈💡😍😇", "😜😱😈🤖🎃",
    "💀👻👽👾🤡", "🤑😷🤠🤓😺", "🙉🙈🙊🦄🐱", "🐶🐼🐨🐯🦁",
    "🐻🐷🐸🐔🐵", "🐧🐦🦆🦉🐲", "🐍🐢🦖🦕🐙", "🦑🦞🦋🐞🦍",
    "🐉🐾🦀🦐🦩", "🦚🦜🦢🦩🐾", "🦊🦝🐁🐀🐇", "🐿️🦔🦇🐉🐲",
    "🐍🐢🦖🦕🦑", "🐟🐠🐡🦈🐬", "🐳🐋🐊🐅🐆", "🦓🦍🦧🦣🦏",
    "🦛🐪🐫🦙🐘", "🦒🐃🐂🐄🐎", "🐖🐏🐑🐐🦌", "🐕🐩🐈🐓🦃",
    "🦚🦜🦢🦩🦮", "🐕‍🦺🦯🐀🐁🐉", "🦊🦝🦘🦡🦥", "🐘🦒🦓🦏🦛",
    "🦜🦢🦩🦩🦚", "🐿️🦨🦥🦦🦩", "🐁🐀🐉🐊🐢", "🐍🐟🐠🐡🦈",
    "🐅🐆🦓🦍🦧", "🦣🦏🦛🐪🐫", "🦙🐘🦒🦓🦍", "🦧🦣🦏🦛🐪",
    "🐖🐏🐑🐐🦌", "🐕🐩🐈🐓🦃", "🦚🦜🦢🦩🦮", "🐕‍🦺🦯🐀🐁🐉",
    "🦊🦝🦘🦡🦥", "🐘🦒🦓🦏🦛", "🦜🦢🦩🦩🦚", "🐿️🦨🦥🦦🦩",
    "🐁🐀🐉🐊🐢", "🐍🐟🐠🐡🦈", "🐅🐆🦓🦍🦧", "🦣🦏🦛🐪🐫",
    "🦙🐘🦒🦓🦍", "🦧🦣🦏🦛🐪", "🐖🐏🐑🐐🦌", "🐕🐩🐈🐓🦃",
    "🦚🦜🦢🦩🦮", "🐕‍🦺🦯🐀🐁🐉", "🦊🦝🦘🦡🦥", "🐘🦒🦓🦏🦛",
    "🦜🦢🦩🦩🦚", "🐿️🦨🦥🦦🦩", "🐁🐀🐉🐊🐢", "🐍🐟🐠🐡🦈"
]

tagging_active = {}

@client.on(events.NewMessage(pattern=r'\.emtag\s*(.*)'))
async def emoji_tag(event):
    if not is_owner(event):
        return
    global tagging_active
    message = event.pattern_match.group(1) or ""
    
    chat_id = event.chat_id
    tagging_active[chat_id] = True 
    
    await event.edit("**𐂡 卄ㄖ丂ㄒ𓅆 `userbot aktivləşdi...` \n Emoji ilə Etiketləmə başladılır**")
    
    tag_count = 0
    max_tags = 100  
    
    try:
        participants = []
        async for user in client.iter_participants(event.chat_id):
            participants.append(user)
        
        selected_users = random.sample(participants, min(len(participants), max_tags))
        
        for user in selected_users:
            if not tagging_active.get(chat_id):  
                break

            emoji = random.choice(emojiler)
            await asyncio.sleep(2)  
            await event.respond(f"[{emoji}](tg://user?id={user.id}) {message}")
            tag_count += 1
        
        if tagging_active.get(chat_id):  # Etiketleme durdurulmamışsa tamamlandı mesajı gönder
            await event.edit(f"✅ **Etiketleme tamamlandı! \n{tag_count} nəfər etiketləndi.**")
    
    except Exception as e:
        await event.reply(f"🚫 Xəta: {str(e)}")
    
    finally:
        tagging_active[chat_id] = False 

@client.on(events.NewMessage(pattern=r'\.tagstop'))
async def stop_tagging(event):
    if not is_owner(event):
        return
    global tagging_active
    chat_id = event.chat_id
    tagging_active[chat_id] = False 
    await event.reply("🚫 **Etiketleme prosesi dayandırıldı!**")

# pm mesaj gonderme 

@client.on(events.NewMessage(pattern = r'\.pm'))
async def pm_message(event):
    if not is_owner(event):
        return
    if event.is_reply:
        reply_message = await event.get_reply_message()
        user_id = reply_message.sender_id
        message = " ".join(event.message.message.split()[1:])
    else:
        args = event.message.message.split()
        if len(args) < 3:
            await event.edit("**Istifadəçi** `və` **mesaj** `daxil etməlisiniz!`")
            return
        target_user = args[1]
        message = " ".join(args[2:])

        if target_user.startswith("@"):
            try:
                user = await client.get_entity(target_user)
                user_id = user.id
            except Exception as e:
                await event.edit(f"`İstifadəçi tapılmadı`: {str(e)}")
                return
        else:
            try:
                user_id = int(target_user)
            except ValueError:
                await event.edit("`Yalnış istifadəçi İD'si`")
                return
    try:
        await client.send_message(user_id,message)
        await event.edit("`Mesaj uğurla göndərildi`")
    except Exception as e:
        await event.edit(f"Mesaj göndərilmədi: {str(e)}")

# pm mesajlari toplu silme

exclude_ids = [7311719460, 7014466635]  

@client.on(events.NewMessage(pattern=r'\.delpm', outgoing=True))
async def delete_private_messages(event):
    deleted_count = 0
    await event.edit("**Şəxsi mesajları iki tərəfli silməyə başlayıram...**")
    await asyncio.sleep(2)

    async for dialog in client.iter_dialogs():
        if dialog.is_user and dialog.entity.id != exclude_ids:
            user = await client.get_entity(dialog.id)
            user_name = user.first_name
            
            messages = []
            async for message in client.iter_messages(dialog.id):
                messages.append(message.id)
            
            if messages:
                try:
                    await client.delete_messages(dialog.id, messages, revoke=True)
                    deleted_count += len(messages)
                    await event.edit(f"**{user_name}** ilə olan mesajlar silindi ✅ | Ümumi silinən mesaj sayı: **{deleted_count}**")
                    await asyncio.sleep(1)  
                    await client.delete_dialog(dialog.id)  
                except:
                    continue

    await event.edit(f"**Bütün uyğun şəxsi mesajlar silindi. Ümumi silinən mesaj sayı:** {deleted_count}")

# xatirlatma

async def send_reminder(event, delay, message):
    await asyncio.sleep(delay)
    await event.reply(f"⏰ Xatırlatma: {message}")

@client.on(events.NewMessage(pattern = r'\.reminder (\d+[smhd]) (.+)'))
async def reminder_command(event):
    if not is_owner(event):
        return
    match = re.match(r'\.reminder (\d+[smhd]) (.+)', event.raw_text)
    if match:
        time_str = match.group(1)
        reminder_message = match.group(2)

        unit = time_str[-1]
        value = int(time_str[:-1])
        if unit == 's':
            delay = value
        elif unit == 'm':
            delay = value * 60
        elif unit == 'h':
            delay = value *60 *60
        elif unit == 'd':
            delay = value * 60 * 60 * 24
        else:
            await event.edit("**Xahiş edirəm mesaj və ya vaxt fromatı daxil edin\n '1s', '1m', '1h', '1d' ")
            return
        
        await event.edit(f"✅ {value}{unit} sonra sənə xatırlatma edəcəm: {reminder_message}")
        await send_reminder(event,delay,reminder_message)
    else:
        await event.edit("Komutun formsatı yalnışdır!\n Doğru format: `.reminder [zaman] [mesaj]`")

# sayac komutu

def parse_time(time_str):
    try:
        parts = time_str.split(":")
        if len(parts) == 1:  # Yalnız saniyələr
            seconds = int(parts[0])
            return seconds
        elif len(parts) == 2:  # Dəqiqə və saniyələr
            minutes = int(parts[0])
            seconds = int(parts[1])
            return minutes * 60 + seconds
        elif len(parts) == 3:  # Saat, dəqiqə və saniyələr
            hours = int(parts[0])
            minutes = int(parts[1])
            seconds = int(parts[2])
            return hours * 3600 + minutes * 60 + seconds
        else:
            return None
    except ValueError:
        return None

def stylize_text(text):
    return f"✨ **{text}** ✨"

def format_remaining_time(total_seconds):
    if total_seconds >= 3600:  # Saat varsa
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours} saat {minutes} dəqiqə {seconds} saniyə"
    elif total_seconds >= 60:  # Dəqiqə varsa
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes} dəqiqə {seconds} saniyə"
    else:  # Yalnız saniyə varsa
        return f"{total_seconds} saniyə"

@client.on(events.NewMessage(pattern=r'\.timer (.+)', forwards=False))
async def timer(event):
    if not is_owner(event):
        return
    try:
        time_str = event.pattern_match.group(1)
        total_seconds = parse_time(time_str)
        
        if total_seconds is None:
            await event.edit(stylize_text("Yanlış zaman formatı! Lütfən, saat:dəqiqə:saniyə formatında daxil edin."))
            return

        user = await client.get_entity(event.sender_id)
        if user.username:
            user_mention = f"@{user.username}"
        else:
            user_mention = f"[{user.first_name}](tg://user?id={user.id})"
        
        remaining_time = format_remaining_time(total_seconds)
        sent_message = await event.respond(stylize_text(f"Taymer başladı: {remaining_time} qaldı."))

        while total_seconds > 0:
            await asyncio.sleep(1)
            total_seconds -= 1

            remaining_time = format_remaining_time(total_seconds)
            await client(EditMessageRequest(
                peer=event.chat_id,
                id=sent_message.id,
                message=stylize_text(f"Taymer başladı: {remaining_time} qaldı.")
            ))

        await event.edit(stylize_text(f"Zaman bitdi! {user_mention}"))
    except Exception as e:
        await event.edit(stylize_text(f"Xəta baş verdi: {str(e)}"))

# qrup sifirlama

@client.on(events.NewMessage(pattern=r'\.reset', outgoing=True))
async def reset_command(event):
    if not is_owner(event):
        return
    loading_message = await event.respond("𐂡 卄ㄖ丂ㄒ𓅆 `userbot`\n✨ **Yüklənir: 0%**")
    
    for i in range(1, 101):
        await asyncio.sleep(0.10)
        await loading_message.edit(f"𐂡 卄ㄖ丂ㄒ𓅆 `userbot`\n✨ **Yüklənir: {i}%**")

    chat = await event.get_chat()
    if isinstance(chat, (Chat, Channel)):
        participants = await client.get_participants(chat)
        total_members = len(participants)
        
        message = await loading_message.reply(f"𐂡 卄ㄖ丂ㄒ𓅆 `userbot`\n✨ **{total_members} istifadəçi çıxarılır...**")
        
        for i in range(total_members, 0, -1):
            await asyncio.sleep(0.05)
            await message.reply("**qrup sıfırlanır**")
            await message.edit(f"𐂡 卄ㄖ丂ㄒ𓅆 `userbot`\n✨ **{i} istifadəçi çıxarılır...**")

    await message.edit("𐂡 卄ㄖ丂ㄒ𓅆 `userbot`\n✨ **Qrup 4 saat ərzində silinəcək.**")

# cihaz prosessor yoxlanisi

@client.on(events.NewMessage(pattern=r'\.pros'))
async def processor(event):
    if not is_owner(event):
        return
    try:

        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=True)
        cpu_freq = psutil.cpu_freq().current

        report = (
            f"🖥 **Processor report**:\n\n"
            f"🔍 **Usage Percentage:** `{cpu_percent}%`\n"
            f"⚙️ **Number of Cores:** `{cpu_count}`\n"
            f"📊 **Frequency:** `{cpu_freq} MHZ`\n"
        )

        await event.edit(report)

    except Exception as e:
        await event.edit(f"🚫 Xəta baş verdi: {str(e)}")

# ilk ad ve username deyisme

@client.on(events.NewMessage(pattern = r'\.setname\s+(.+)$'))
async def set_name(event):
    if not is_owner(event):
        return
    new_name = event.pattern_match.group(1).strip()

    try:
        await client(functions.account.UpdateProfileRequest(
            first_name = new_name
        ))
        await event.edit(f"**🎉 İlk adınız uğurla `{new_name}` olaraq dəyişdirildi**")
    except Exception as e:
        await event.edit(f"**⚠️ Adınız dəyişdirilərkən bir xəta baş verdi: {str(e)}**")

@client.on(events.NewMessage(pattern = r'\.setusername\s+(.+)$'))
async def set_username(event):
    if not is_owner(event):
        return
    new_username = event.pattern_match.group(1).strip()

    try:
        await client(functions.account.UpdateUsernameRequest(
            username = new_username
        ))
        await event.edit(f"**🎉 Istifadəçi etiketiniz uğurla `{new_username}` olaraq dəyişdirildi**")
    except errors.UsernameOccupiedError:
        await event.edit(f"**🚫 Etiketi daha əvvəl istifadə edilib\n`{new_username}`**")
    except Exception as e:
        await event.edit(f"**Xəta:**{str(e)}")

# fake eylemler

ALIVE_NAME = "admin"

@client.on(events.NewMessage(pattern=r"\.fake(?:\s|$)([\s\S]*)"))
async def saxta(event):
    if not is_owner(event):
        return
    options = ["typing", "record-audio", "game", "location", "record-round", "record-video"]
    input_str = event.pattern_match.group(1).split()
    
    saxta_emel = choice(options) if len(input_str) == 0 else input_str[0].lower()
    saxta_muddet = randint(300, 360) if len(input_str) <= 1 else int(input_str[1])
    
    try:
        if saxta_muddet > 0:
            await event.delete()
            async with client.action(event.chat_id, saxta_emel):
                await asyncio.sleep(saxta_muddet)
    except ValueError as e:
        # Xətanın nə olduğunu göstərən mesaj
        await event.reply(f"Xəta baş verdi!: {str(e)}")
    except Exception as e:
        await event.reply(f"Xəta baş verdi!: {str(e)}")

# İdarəçi təyin edir kimi göstərən animasiya funksiyası
@client.on(events.NewMessage(pattern=".admin$"))
async def pidaadmin(event):
    if not is_owner(event):
        return
    animation_sure = 1
    animation_steps = [
        "**İstifadəçi idarəçi kimi təyin edilir...**",
        "**Bütün səlahiyyətlər verilir...**",
        "**(1) Mesaj göndərmək: ✅**",
        "**(2) Media göndərmək: ✅**",
        "**(3) Stikerlər və GIF göndərmək: ✅**",
        "**(4) Sorğu göndərmək: ✅**",
        "**(5) Linklər yerləşdirmək: ✅**",
        "**(6) İstifadəçiləri əlavə etmək: ✅**",
        "**(7) Mesajları sancılamaq: ✅**",
        "**Səlahiyyətlər uğurla verildi!**",
        f"**Təyin edildi: {ALIVE_NAME}**",
    ]
    
    for step in animation_steps:
        await asyncio.sleep(animation_sure)
        await event.edit(step)

# qız adları

azerbaycan_kiz_isimleri = [
    "Aygün", "Leyla", "Günel", "Narmin", "Fidan", "Sevinc", "Zümrüd", "Gülnar", 
    "Nigar", "Zehra", "Lalə", "Nazlı", "Şəbnəm", "Ülviyyə", "Elvina", "Kamilla", 
    "Ayşen", "Mehriban", "Aysel", "Rəna"
]

emojiler = ["🌸", "💐", "🌹", "🌺", "💮", "🌻", "🌼", "🌷", "🌞", "💫"]

@client.on(events.NewMessage(pattern=r"\.atvall"))
async def atval(event):
    mesaj = ""
    
    for isim in azerbaycan_kiz_isimleri:
        emoji = random.choice(emojiler)
        
        mesaj += f"{emoji} {isim}\n"
        
        await event.edit(mesaj)
        
        await asyncio.sleep(1)

# salam

MESAJ_METNI = "Salam xoş gəlmisiniz həmişə siz gələsiniz.Necəsiz?"

@client.on(events.NewMessage)
async def oyun_mesaji(event):
    if event.raw_text.strip().lower() == "salam" and not event.sender.bot:
        try:
            await event.reply(MESAJ_METNI)
        except Exception as e:
            print(f"Mesaj gönderilemedi: {e}")

print("bot aktivdir")
client.start()
client.run_until_disconnected()