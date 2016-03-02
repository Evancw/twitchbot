# Send chat message to server
def chat(sock, msg):
      sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

# Ban user
def ban(sock, user):
    chat(sock,".ban {}".format(user))

# Timeout user
def timeout(sock, user, secs=300):
    chat(sock, ".timeout {}".format(user, secs))
