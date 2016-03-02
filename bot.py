import cfg
import socket
import time
import re

# Define regex to find user messages
USER_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")


def main():
    chat = socket.socket()
    chat.connect((cfg.HOST, cfg.PORT))
    chat.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    chat.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    chat.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

    while True:
        incoming_response = chat.recv(1024).decode("utf-8")
        if incoming_response == "PING :tmi.twitch.tv\r\n":
            chat.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", incoming_response).group(0)
            message = USER_MSG.sub("", incoming_response)
            print(username, ":", message)

    time.sleep(1 / cfg.RATE)


main()
