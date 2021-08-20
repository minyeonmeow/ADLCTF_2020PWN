# 2020-pwn

PWN for 2020 NCU ADL CTF

# Setup

- Run `sudo docker build -t ctf .` to build the docker image template "ctf".
- Run `sudo ./setup_all_container.sh up` to bring the challenges online.

 
# Problem Set
### helloctf
- Author: genesis
- Tricks: bof
- Points: 0
- Port: 11001
 
### helloctf_again
- Author: genesis
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

### libccc
- Auther: davidhcefx
- Tricks: ret2libc
- Hint:
    - `LD_LIBRARY_PATH=.` 才能正確連結到 **題目所提供的 libc** 而不是你自己電腦上的 libc 喔。
- Description: provide src code
- Points: 100
- Port: 11004

### ANALYZER
- Auther: davidhcefx
- Tricks: shellcoding, NOP sled, avoid "/bin/sh", avoid "int 0x80"
- Description:
    - provides .h file
    - link1: https://defuse.ca/online-x86-assembler.htm
    - link2: https://c9x.me/x86/
- Hint:
    - How to debug Shellcode
        - 先 `gcc -S -masm=intel` 隨便編譯一個 .c 檔
        - 把你的 shellcode 貼在 main 裡面然後編譯成執行檔
        - 開 gdb 來 debug
    - This is a shellcoding challenge.  Don't spend time cracking the cryptosystem :-) (unless you want to) Hint2: There are overflows in the program!
- Points: 50
- Port: 11005

### family
- Author: minyeonmeow
- Tricks: ROP, leak canary, stack pivot
- Hint:
    - try to find our similarity
- Points: 100
- Port: 11006

### podcast
- Auther: davidhcefx
- Tricks: fmt-string, pivoting, ROP, ret2libc
- Description:
    - provide src code (within python comment)
    - <p>TOP 50 PODCASTS IN TAIWAN, BEST PODCAST CHANNELS IN TAIWAN, 2020 BEST QUALITY TAIWAN PODCASTS, HOT NEW PODCAST CHANNEL TAIWAN 2020, TOP 50 MOST POPULAR PODCAST CHANNEL IN TAIWAN, LIST OF BEST 50 PODCAST CHANNELS YOU SHOULD NOT MISS, LISTEN TO THE BEST QUALITY PODCASTS RIGHT NOW FOR FREE, BEST 50 PODCASTS IN TAIWAN FOR FREE, TOP RATED 50 PODCAST CHANNEL IN TAIWAN, MOST VIRAL PODCAST CHANNEL IN TAIWAN, BEST PODCAST LIST FREE DOWNLOAD</p>
- Hint:
    - Don't spend too much time on the Bash or Python code. Just pwn the server!!
    - Do you know that other than rip, rbp is also controllable? (aka pivoting)
    - Tricks you probably:
        - would use: Shellcode, ROP, ret2text, ret2libc, GOT, Pivoting, Format-string, Integer overflow.
        - wouldn't use: UAF, Double-Free, Chunk overlay, Off-by-one, malloc_hook.
- Points: 50
- Port: 11007


# 配分

- 每題均一價 100 points:
    - CTFd 得分: 30%
    - demo 回答程度: 70%
        - 有來至少就有一半的分數 (35%)
        - 回答不出來者, 我們會視情況允許補交報告加分。

- podcast 跟 ANALYZER 這兩題太少人解開, 最後調成各 50 points


# Demo

- 一組 20 min (但感覺有點緊縮)
    - 實驗室學弟妹最好安排雙倍時間, 因為通常喜歡問得特別深 (?)

- 額外: 每組會選解開最多 / 投入最多的學生額外 +5 project 總分
    - (目的是為了優先交接攻防助教給會打 CTF 者哈哈)

- Demo 問題參考:
    - Hello ctf again:
        1. 為什麼不能跳到最開始的地方 (stack alignment)
        2. system 跟 execve 的差別 (system 是 fork 新 process, execve 是把目前 process 取代)
        3. execve 後面兩個參數的作用
        4. 這題的資安漏洞在哪裡? (有些人不清楚問題本身)
    - Lucky system:
        1. 哪裡壞掉
        2. lea 跟 mov 的差別
        3. 說明一下 library function 第一次被呼叫時會發生什麼事情? 第二次呢?
        4. plt 段可寫嗎? 那 GOT 段呢?
    - Family:
        1. 所以相同點是?
        2. canary 一般會放在 stack 段哪裡? 從哪裡取出的?
        3. 不同的 process canary 會相同嗎? 那不同 thread 呢? (thread 會因為 fs 存的位置是 data 段會 share)
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
