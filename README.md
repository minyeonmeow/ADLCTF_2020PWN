# 2020-pwn

PWN for 2020 NCU ADL CTF

# Setup

- Run `sudo docker build -t ctf .` to build the docker image template "ctf".
- Run `sudo ./setup_all_container.sh up` to bring the challenges online.

 
# Problem Set
### helloctf
- Author: minyeonmeow
- Tricks: bof
- Points: 0
- Port: 11001
 
### helloctf_again
- Author: minyeonmeow
- Tricks: bof, movaps
- Hint:
    - Use Ubuntu 18.04.
    - Open up gdb, trace it until you know why.
- Points: 100
- Port: 11002

### lucky_system
- Author: minyeonmeow
- Tricks: GOT hijack
- Hint:
    - Ummm...I think there are some bugs in my code...
- Points: 100
- Port: 11003

### family
- Author: minyeonmeow
- Tricks: ROP, leak canary, stack pivot
- Hint:
    - try to find our similarity
- Points: 100
- Port: 11006

# Demo
- Demo 問題參考:
    - Hello ctf and again:
        1. 為什麼不能跳到最開始的地方 (stack alignment)
        2. system 跟 execve 的差別 (system 是 fork 新 process, execve 是把目前 process 取代)
        3. execve 後面兩個參數的作用 (第二個參數是arg，第三個參數是envp)
        4. 這題的資安漏洞在哪裡? (`gets()`不會限制輸入，宣告的buffer又不夠大造成使用者可以輸入超出buffer大小甚至蓋到return address (buffer overflow))
    - Lucky system:
        1. 哪裡壞掉 (scanf後面參數是一個address(scanf(..., &x))，但我們直接寫成scanf(..., x)，會造成直接將輸入的東西寫在這個位置上)
        2. 如何解? (利用上面的bug，將我們要跳到的地方(execve()的位置))直接寫在GOT中`fflush`的位置(其他後面會使用的function也可以)，這樣下一行在執行`fflush()`時就會跳到`execve()`
        4. lea 跟 mov 的差別 (lea a, b == mov a, [b])
        5. 說明一下 library function 第一次被呼叫時會發生什麼事情? 第二次呢?
           1. 跳到fun@plt，進GOT後發現沒有，會跳進`dl_runtime_resolve()`取得函數的絕對位置，並寫進GOT中對應的位置
           2. 可以直接從GOT取得函數的絕對位置
        6. plt 段可寫嗎? 那 GOT 段呢? (plt不行，got可寫)
    - Family:
        1. 所以相同點是? (parent跟child的canary相同)
        2. 如何解? (先利用child leak出canary，再利用這個canary在parent地方達成ROP，但因為空間不夠，需要利用stack pivot將stack移動到bss段上，因為bss可寫)
        3. 如何leak canary? (因為canary的第一個byte是0x0，而`read()`會讀到0x0截斷，因此如果這邊把canary第一個byte蓋掉，可以leak出接下來的7byte，前面加上0x0就是canary)
        4. canary 一般會放在 stack 段哪裡? (放在return address之前，這樣才可以避免使用者輸入蓋到return address) 從哪裡取出的? (fs+0x28)
        5. 不同的 process canary 會相同嗎? 那不同 thread 呢? (thread 會因為 fs 存的位置是 data 段會 share)
    - Libccc:
        1. 這題有哪些漏洞?
        2. write 的三個參數分別代表什麼?
    - Podkest:
        1. 這題有哪些漏洞?
        2. (fmt-str 可以 leak 哪些東西?)
        3. 一開始的檔案為什麼可以雙擊? (你們有發現嗎?)
        4. 既然可以 overflow，為什麼不直接寫 shellcode 就好了? (NX)


# 小叮嚀

- 不要通靈, 盡量用 "教育意義" 的角度來思考 (https://www.youtube.com/watch?v=L1RvK1443Yw)
- CTF 設計手冊: https://docs.google.com/document/d/1QBhColOjT8vVeyQxM1qNE-pczqeNSJiWOEiZQF2SSh8/preview
- CTFd 動態配分會讓最終分數相差懸殊, 不太適合. 可以考慮均一價 100, 強調基礎功跟進階技巧同等重要.
- 給對組語陌生的新手, 偶爾還是提供一下 src 比較好.
