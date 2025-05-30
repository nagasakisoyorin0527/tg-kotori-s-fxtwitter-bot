# tg-soyorin-fxtwitter-bot
A Telegram bot that improves link previews for **X (Twitter)** and **Bilibili** by automatically replacing URLs and replying with the modified message.

## Features
- Detect x.com. twitter.com, bilibili.com and b23.tv URL in the message
- Process the message by:
  - change x.com to fixupx.com and twitter.com to fxtwitter.com
  - Remove bilibili.com's UTM automatically and then change to bilibilibb.com
  - Expand b23.tv (short URL of bilibili.com), remove UTM and change to bilibilibb.com

## Example
<pre>
Original message:
  Nice picture: https://x.com/user_name/status/abc123

Modified message: 
  Sender's name:
  Nice picture
  https://fixupx.com/user_name/status/abc123
</pre>

# How to use
## Access via share link:
- https://t.me/Soyorin_FxTwitter_Bot <br />
- Invite the bot to a group
- Allow the bot to read and delete messages
## Setup your own bot
- Install telegram-bot-python
- Download the file "soyorin_fxtwitter_bot.py"
- Replace TOKEN with your bot's token and run the file
- Keep it running
- Access the bot by DM it or invite it to a group

#
fxtwitter & fixupx are made by https://github.com/FxEmbed/FxEmbed <br />
bilibilibb is made by: https://bilibilibb.com/
