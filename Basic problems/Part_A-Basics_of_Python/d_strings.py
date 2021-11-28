# Strings:
# ========
msg = "This,Is,A,Message."

print(len(msg))

msg2 = msg.capitalize()

print(msg2)

print(msg.upper())

print(msg.lower())

msg3 = msg.split(',')

print(msg3)

print('-'.join(msg3))

print(msg.isdigit())


# OUTPUT:
# 18
# This,is,a,message.
# THIS,IS,A,MESSAGE.
# this,is,a,message.
# ['This', 'Is', 'A', 'Message.']
# This-Is-A-Message.
# False