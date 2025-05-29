#This bot is made by nagasakisoyorin0527
#Remember to replace TOKEN with your bot token from BotFather on Telegram
#Use pip install python-telegram-bot to install the essential library

import logging
import re
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import BadRequest

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
http_headers = {"Accept": "*/*", "Connection": "keep_alive", 
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

#Processing bilibili.com and b23.tv URLs
def remove_bilibili_tracking(url: str):
    return url.split("?")[0]

def search_b23_url(message):
    expression = r"https://b23\.tv/\S+"
    match = re.search(expression, message)
    return match.group()
    
def get_url(url):
    rs = requests.get(url, headers=http_headers)
    remove_tracking = remove_bilibili_tracking(rs.url)
    return remove_tracking

# Replace with your bot token
TOKEN = "7911645407:AAEs5M1H-CVY0MBClHiXwSNJaau98ldg1_Q"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        'Hi! Welcome to use this bot. Use "/help" to get more information'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "Welcome to use Soyorin's Fxtwitter Bot!\n"
        "This bot is made by GitHub user nagasakisoyorin0527\n"
        "The bot will edit and reply (delete the original message if possible) x.com, twitter.com, bilibili.com and b23.tv URLs"
        "For more detailed information, visit https://github.com/nagasakisoyorin0527/tg-soyorin-fxtwitter-bot"
        "Use /ping to chekc whether the bot is online"
    )

async def pingpong(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text('pong')


async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return
    
    message_text = update.message.text
    modified = False
    
    # Check for x.com URLs that don't have "fixupx.com"
    if "https://x.com/" in message_text and "https://fixupx.com/" not in message_text and "status" in message_text:
        message_text = message_text.replace("https://x.com/", "https://fixupx.com/")
        modified = True
    # Check for twitter.com URLs that don't have "twitter.com"
    if "https://twitter.com/" in message_text and "https://fxtwitter.com/" not in message_text and "status" in message_text:
        message_text = message_text.replace("https://twitter.com/", "https://fxtwitter.com/")
        modified = True
    
    #Check if the URL is sharing a Bilibili video
    if "bilibili.com/video" in message_text and "bilibilibb.com" not in message_text:
        message_text=remove_bilibili_tracking(message_text)
        message_text = message_text.replace("bilibili.com", "bilibilibb.com")
        modified = True
    if "https://b23.tv/" in message_text:
        url = search_b23_url(message_text)
        real_url = get_url(url)
        message_text = message_text.replace(url, real_url)
        message_text = message_text.replace("bilibili.com", "bilibilibb.com")  
        modified = True 

    #reply and delete the original message if detected the URL
    if modified:
        logger.info(f"Modified message: {message_text}")
        
        # Get the sender's name
        sender_name = update.message.from_user.first_name
        if update.message.from_user.last_name:
            sender_name += " " + update.message.from_user.last_name
            
        # Format message with sender's name
        formatted_message = f"{sender_name}:\n{message_text}"
        try:
            # First reply to the person
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=formatted_message
            )
            # Then try to delete the original
            await update.message.delete()
            logger.info("Used delete and resend approach")
        except BadRequest as e:
            logger.warning(f"Couldn't delete original message: {e}")

#Debugging commands
async def debug_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    bot_permissions = await context.bot.get_my_member(chat_id=chat_id, user_id=context.bot.id)
    
    permissions_text = f"Bot permissions in this chat:\n{bot_permissions.to_dict()}"
    await update.message.reply_text(permissions_text)

#main function
def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("debug", debug_command))
    application.add_handler(CommandHandler("ping", pingpong))
    
    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
