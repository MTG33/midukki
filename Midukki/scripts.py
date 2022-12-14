START_TXT = """
Hello π {mention} 

I'm <b>{bot}</b> β¨ an advanced telegram Group management

I'm here to help you manage your groups! Hit /help to find out more about how to use me to my full potential..!

Join <b><a href=http://t.me/MTG33BOTZ>my news channel</a></b> to get information on all the latest updates
"""

HELP_TXT = """
π <b>Hello {mention}!</b>

I Can Guide You Through All Of <b>{bot}</b>'s Cool Features And How To Properly Use Them. Use The Buttons Below To Navigate Through All Of The Modules          

π <u><b>HelpFull Commands</b></u>:

- /start : Starts me! You've probably already used this!.
- /help : Sends this message; I'll tell you more about models!
- /about : Sends this message; I'll tell you more about myself!
- /donate : Gives you info on how to support me and my creator!

<b>All commands can be used with the following: [ / ]</b>
"""

ABOUT_TXT = """
[{name}](t.me/{username}) Was created on September 4, 2022
We are currently developing this bot, using only the Pyrogram library.

βΎ Developers : Muhammed
βΎ Language : Python3
βΎ Framework : Pyrogram
βΎ Database : Mongo db
"""

DONATE_TXT = """
If you like this project of mine, you can donate by clicking on the given link

Dev : [MTG33](t.me/MTG33)
CONNECT ME π AND SEND ME COFFEE  : [Click Here](https://t.me/MTG33)
  or SEND THIS BOT TO OTHERSπ₯π₯ `t.me/MADARA_RoBot`
"""

STATUS_TXT = """
**--{bot}'s STATUS--**

π‘ __--Server Status--__
β Uptime: `{a}`
β CPU Usage: `{b}%`
β RAM Usage: `{c}%`
β Total Disk Space: `{d}`
β Used Space: `{e} ({f}%)`
β Free Space: `{g}`

ποΈ __--Database Status--__
β Tota Files: `{h}`
β Tota Users: `{i}`
β Tota Chats: `{j}`
β Used Storage: `{k}` 
β Free Storage: `{l}`
β Total Storage: `{m}` 
"""

AUTO_TXT = """
**--MODULE OF AUTOFILTER--**

β I Can Provide Files In Your Group, It Very Easy Way Just Add Me Ro Your Group And Make Me Admin In Your Group, Thats All.. I Will Provide Files From Your Group 
      
π **--Usage & Commands--** :

β /autofilter : use to turn on & off
β /set_temp : set new result temp
β /del_temp : del seted result temp
β /settings : use to modify autofilter settings

π **--Supporting Vars--** :

 β’ `{mention}` : user profile link
 β’ `{query}` : request text
 β’ `{group_name}` : group name
"""

MANUAL_TXT = """
**--MODULE OF MANUALFILTER--**

β Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Bot Will Respond Whenever A Keyword Is Found The Message

π **--Note--** :

1. This bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

π **--Commands and Usage--** :

β /add : add a filter in chat
β /filters : list all the filters of a chat
β /del : delete a specific filter in chat
β /delall : delete the whole filters in a chat (chat owner only)
"""

CONNECTION_TXT = """
**--MODULE OF CONNECTIONS**--

β Used to connect bot to PM for managing filters 
β it helps to avoid spamming in groups.

π **--NOTE--** :

1. Only admins an add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

π **--Commands and Usage--** :

β /connect : connect a particular chat to your PM
β /disconnect : disconnect from a chat
β /connections : list all your connections
"""

INFO_TXT = """
**--MODULE OF INFO--**

β Hese are the extra features of this bot

π **--Commands and Usage--** :

β /id : get id of a specifed user.
β /info : get information about a user.
"""

SPELL_TXT = """
**--MODULE OF SPELLCHECK--**

β Everything Related To The Spell Check Module When No AutoFilter Result Are Found 

π **--Commands & Usage--** :

β /set_spell : Set A New SpellCheck Text
β /del_spell : restart Spell Check Message

π **--Supporting Vars--** :

 β’ `{mention}` : user profile link
 β’ `{query}` : request text 
 β’ `{title}` : get chat title

> Eg:- /setspell Check Your Spelling {query}
"""

CAP_TXT = """
**--MODULE OF CUSTOM CAPTION--**

β Use This Feature To Add A Custom Caption To File

π **--Commands & Usage--** :

β /set_cap : set new file caption 
β /del_cap : restart file caption

π **--Supporting Vars--** :

 β’ {mention} : user profile link
 β’ {file_name} : file name
 β’ {size} : file size 
 β’ {caption} : get original caption
"""

MUTE_TXT = """
**--MODULE OF MUTE--** π€

β some people need to be publicly muted: spammers, annkyances, or just trolls...! this module allows you to do that easily by exposing same commo actions, so everyone will see..!

π **--Commands and Usage**-- :

β /mute : Mute a user
β /unmute : Unmute a user
β /tmute : Temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days
"""

BAN_TXT = """
**--MODULE OF BAN--** π«

β some people need to be publicly banned: spammers, annkyances, or just trolls...! this module allows you to do that easily by exposing same commo actions, so everyone will see..!

π **--Commands and Usage**-- :

β /ban : ban a user 
β /unban : unban the user
β /tban : Temporarily ban a user. Example time values: 30s = 30 seconds, 4m = 4 minutes, 3h = 3 hours
"""

PIN_TXT = """
**--MODULE OF PIN--** π

β all the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

π **--Commands and Usage**-- :

β /pin : Pin the message you replied to message to send a notification to group members
β /unpin : Unpin the current pinned message. if used as a reply, unpins the replied to message
"""

ADMIN_PANEL = """
π€ **Admin Only**

- /channel : total channels
- /total : total files
- /delfile : del single files
- /delallfile : del all files
- /skip : skip index file
- /logs : bot logs
- /broadcast : broadcast message
"""

FILE_CAPTION_TXT = """{file_name}"""

SPELLCHECK_TXT = """Hey Mr 
Check Your Spelling 
"""

IMDB_TEMPLATE_TXT = """
πββοΈ Hey {mention} Your Requested {query} is ready π
"""

WELCOME_TXT = """
Hai {mention}

Welcome To {chat} β£οΈ
"""

SEND_LOGS_A = """
#BOT_STARTED"""

class Txt(object):
    START_TXT = START_TXT
    HELP_TXT = HELP_TXT
    ABOUT_TXT = ABOUT_TXT
    STATUS_TXT = STATUS_TXT
    AUTO_TXT = AUTO_TXT
    MANUAL_TXT = MANUAL_TXT
    INFO_TXT = INFO_TXT
    CONNECTION_TXT = CONNECTION_TXT
    CAP_TXT = CAP_TXT
    SPELL_TXT = SPELL_TXT
    MUTE_TXT = MUTE_TXT
    BAN_TXT = BAN_TXT
    PIN_TXT = PIN_TXT
    ADMIN_PANEL = ADMIN_PANEL
