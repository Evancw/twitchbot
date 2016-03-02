# twitchbot
Python based twitch chat moderation bot. To run the bot create a file named "cfg.py" following
the below outline where fields that need to be changed are in CAPITAL letters (leaving double quotes)

--------------------------------
HOST = "irc.twitch.tv"
PORT = 6667
NICK = "TWITCH_USERNAME"
PASS = "OAUTH"              # Generated from https://twitchapps.com/tmi/
CHAN = "#CHANNEL_NAME"

# Set maximum number of msg/30 secs
RATE = 20/30
--------------------------------

commands are contained in the commands.py file, most are automatically called when
appropriate as determined by regex pattern matching.
