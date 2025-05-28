# tg-kotori-s-fxtwitter-bot
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

## How to use
- Install telegram-bot-python
- Run the file "kotoris_fxtwitter_bot.py"
- Keep it running
- Access the bot by DM it or invite it to a group

## 
fxtwitter & fixupx are made by https://github.com/FxEmbed/FxEmbed <br />
bilibilibb is made by: https://bilibilibb.com/
