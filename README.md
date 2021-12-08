# File-Sharing-Bot


***Telegram Bot to Store Posts And Documents And It Can Access By Special Links.
I Guess This Will Be Usefull For Many People....***

##

****If You Need Any More Modes In Repo or If You Find Out Any Bugs, Mention In [@AIOM_BOTS_GROUP](https://t.me/AIOM_BOTS_GROUP)****

### Features
- Fully Customisable.
- Customisable Welcome & Forcesub Messages.
- More than One Posts in One Link.
- Can Be Deployed On Heroku Directly.

### Setup

- Add The Bot To Database Channel With All Permission
- Add Bot To ForceSub Channel As Admin With Invite Users Via Link Permission If You Enabled ForceSub 

##

### Deploy To Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ajvadntr/AIOM-FILE-SHARING-BOT)</br>

### Deploy To Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fajvadntr%2FAIOM-FILE-SHARING-BOT&envs=ADMINS%2CAPI_HASH%2CAPP_ID%2CCHANNEL_ID%2CFORCE_SUB_CHANNEL%2CFORCE_SUB_MESSAGE%2COWNER_ID%2CSTART_MESSAGE%2CTG_BOT_TOKEN&optionalEnvs=ADMINS&ADMINSDesc=A+space+separated+list+of+user_ids+of+Admins%2C+they+can+only+create+links&API_HASHDesc=your+api+hash%2C+take+it+from+my.telegram.org&APP_IDDesc=your+app+id%2C+take+it+from+my.telegram.org&CHANNEL_IDDesc=make+a+channel+%28database+channel%29%2C+then+make+the+bot+as+admin+in+channel%2C+and+it%27s+id+paste+it+here++&FORCE_SUB_CHANNELDesc=id+of+the+channel+or+group%2C+if+you+don%27t+want+to+enable+force+sub+feature+else+put+0&FORCE_SUB_MESSAGEDesc=Optional%3A+Force+Sub+message+of+bot%2C+use+HTML+parsemode+format&OWNER_IDDesc=An+integer+of+consisting+of+your+owner+ID&START_MESSAGEDesc=Optional%3A+start+message+of+bot%2C+use+HTML+parse+mode+format&TG_BOT_TOKENDesc=Your+Bot+token%2C+Get+it+from+%40Botfather&FORCE_SUB_CHANNELDefault=0&FORCE_SUB_MESSAGEDefault=**Hello+%7Bfirst%7D++You+Need+To+Join+In+My+Channel+To+Use+Me**&START_MESSAGEDefault=**Hello+%7Bfirst%7D++I+Can+Store+Private+Files+In+Specified+Channel+And+Other+Users+Can+Access+It+From+Special+Link.**&referralCode=ajvadntr)

### Tutorial

<a href="https://youtu.be/LCrkRTMkmzE">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

**Check This Tutorial Video On YouTube For Any Help**
#### Deploy In Your VPS
````bash
git clone https://github.com/CodeXBotz/File-Sharing-Bot
cd File-Sharing-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users
```

### Variables

* `API_HASH` Your API Hash from my.telegram.org
* `API_ID` Your API ID from my.telegram.org
* `TG_BOT_TOKEN` Your bot token from @BotFather
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/codexbotz/File-Sharing-Bot/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub

### Extra Variables

* `CUSTOM_CAPTION` put your Custom caption text if you want Setup Custom Caption, you can use HTML and <a href='https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Put True to Disable Channel Share Button, Default if False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

### Credits

*****Thanks To [CodeXBotz](https://github.com/CodeXBotz) For This Awesome [Code](https://github.com/CodeXBotz/File-Sharing-Bot)*****
