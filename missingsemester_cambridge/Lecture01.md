# Lecture 1. Course Overview + The Shell

`echo`: 입력한 값을 출력

```shell
$ echo hello
hello
$ echo "hello world" # <=> echo hello\ world (공백을 포함한 값 출력시)
hello world
```

- echo environment variables(환경 변수)
  - 터미널에서 명령어로 사용할 수 있는 이름에 대한 경로를 출력

```sh
$ echo $PATH
/home/iloveslowfood/.pyenv/shims:/home/iloveslowfood/.pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/mnt/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v10.1/...(중략)
```

`which`: 파일에 대한 경로 출력

```shell
$ which echo # echo 명령어의 경로
echo: shell built-in command
```

`pwd`: 워킹디렉토리 출력(print working directory)

```shell
$ pwd
/mnt/c/Users/iloveslowfood
```

`cd`: 디렉토리 이동

```shell
$ cd /home # 홈으로 이동

# 상대경로
$ cd .. # 상위 디렉토리로 이동
$ cd ./home # 하위 디렉토리로 이동

# '~', '-'의 사용
$ cd ~ # 홈디렉토리로 이동
$ cd - # 직전 디렉토리로 이동
```

`ls`: 현재 디렉토리의 모든 파일 목록을 출력

```shell
$ ls
powerlevel10k  projects
$ ls -l # 파일 정보를 더 자세히 볼 수 있음
$ ll # ls -l을 대신하여 사용할 수 있는 alias

# 홈디렉토리 출력 결과
total 8
drwxr-xr-x 6 iloveslowfood iloveslowfood 4096 Jan 10 17:25 powerlevel10k
drwxr-xr-x 3 iloveslowfood iloveslowfood 4096 Jan 18 11:55 projects
           # 접근 권한 가진 # 접근 권한 가진
           # 파일 소유자   # 파일 소유 그룹
           
# 루트디렉토리 출력 결과
total 684
lrwxrwxrwx   1 root root      7 Aug  5 06:39 bin -> usr/bin
drwxr-xr-x   2 root root   4096 Aug  5 06:47 boot
drwxr-xr-x   8 root root   2780 Jan 23 12:32 dev
...
```

`cat`: 텍스트 파일의 내용을 출력

```shell
$ cat hello.txt # <=> cat < hello.txt(hello.txt를 cat에 input한 셈)
```

`help`: 명령어에 대한 도움말 출력

```shell
$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic 
...
```

`mv`: 파일 이름 바꾸기

```shell
$ mv name_origin.md name_changed.md
```

`cp`: 파일 복사

```shell
# cp <복사할 파일 경로> <복사본 파일 경로>
$ cp file_origin file_copy
```

`rm`: 파일 삭제

```shell
$ rm file_remove # 파일 삭제
$ rm -r directory # --recursive: 해당 디렉토리 내 모든 파일까지 삭제
$ rmdir # 빈 폴더 삭제
```

`man`: 명령어의 매뉴얼을 확인할 수 있음

- `q` 또는 `quit`을 통해 매뉴얼을 나갈 수 있음

```shell
$ man ls
NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information about the FILEs (the current directory by default).  Sort entries alphabetically 
...
```

Input Stream, Output Stream

- Input Stream: 입력값을 넣는 스트림(default: 키보드)
- Output Stream: 결괏값이 출력되는 스트림(default: 터미널, `echo` 출력값이 그래서 터미널에 출력되는 것)
- 얘네를 다뤄보자: `>`, `<`, `|` 등 활용
  - `>>`: append

```shell
$ echo hello > hello.txt # echo 결과가 터미널에 나오는 것이 아닌 hello.txt에 기록됨
$ cat < hello.txt > hello2.txt # <=> cp hello.txt hello2.txt
$ cat < hello.txt >> hello2.txt # hello2.txt에 hello.txt 내용 append
$ ls -l / | tail -n1 # | 연산자를 통해 좌측의 output을 우측 명령어의 input으로 넣을 수 있음
```

`sudo`: Super User Do, 루트 유저로서 명령어를 실행

```shell
sudo su # 사용자를 루트유저로 변경
```

`xdg-open`: 사용자가 선호나는 파일이나 URL을 연다

> Reference

[Lecture 1: Course Overview + The Shell (2020)](https://www.youtube.com/watch?v=Z56Jmr9Z34Q&t=419s)

[linux tee 명령어 사용법](https://www.lesstif.com/lpt/linux-tee-89556049.html)

> Attitude & Tips

- `/usr/bin`: 루트 디렉토리
  - 윈도우에서는 파티션당 하나의 루트 디렉토리가 존재(`C:\`, `D:\`, ...)

- `~`: 홈디렉토리를 의미
- `drwxr-xr-x`: 권한정보를 나타내는 방식. 해당 파일에 어떤 권한이 부여되어 있는지 확인 가능
  - 총 4부분으로 나누어 해석: `d` + `rwx` + `r-x` + `r-x`
  - 첫 `d`: 디렉토리
    - [?] `l`도 있는데 이건 뭐지?
  - 둘째 3글자(`rwx`): 소유자가 접근할 수 있는 권한
  - 셋째 3글자(`r-x`): 그룹에 속한 사용자들 접근 권한
  - 넷째 3글자(`r-x`): 모든 사용자가 접근할 수 있는 권한
  - 해당 위치가 `-`로 표기되어 있으면 해당 권한이 없는 것을 의미
  - 이진수로 `r` 은 4, `w`는 2, `x`는 1의 값을 가짐
- 루트 유저: 시스템 내 모든 것을 할 수 있음
- `/sys`: 컴퓨터의  코어 파일들을 확인할 수 있음
  - 여기 있는 파일을은 `sudo` 프로그램이 아니기 때문에, 조작이 불가능함
    - Shell에서 출력을 redirection할 경우 `sudo`를 사용해도 일반 사용자로 전환되어 루트 권한으로 파일에 쓰거나 내용 추가가 필요한 경우 제대로 동작하지 않음
    - `tee`를 사용할 경우 동작하지 않는 문제를 해결할 수 있음
      - `echo "hello" | tee OUTFILE`: echo를 통해 출력한 'hello'를 OUTPUT에 기록
  - `#` 심볼을 활용함
  - 또는 `sudo su` 명령어를 통해 루트 사용자로 shell에 접속
  - [?] `sudo tee` <- 이게 뭐지? 42분 32초 부분

