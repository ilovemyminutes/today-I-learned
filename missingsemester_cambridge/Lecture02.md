# Lecture 2. Shell Tools and Scripting

- 변수 할당과 출력

```shell
$ foo=bar # 띄어쓰기는 놉! 명령어로 인식함
$ echo $foo
bar

$ echo "hello" # 큰따옴표
hello

$ echo 'world' # 작은따옴포
world

$ echo "value is $foo" # 파이썬의 문자열 포매팅과 같은 맥락
value is bar

$ echo 'value is $foo' # 주의! 작은 따옴표는 포매팅 불가능
value is $foo
```

- 함수 정의

```shell
$ vim mcd.sh

mcd(){
	mkdir -p "$1" # [?] 1의 의미가 뭐지?
	cd "$1"
}

:wq

$ source mcd.sh
$ mcd test
$ /test
```

- `echo $?`

```shell
$ echo $? # 스크립트가 있으면 1, 없으면 0을 출력							
0

$ false
$ echo $?
1 # [?] 왜 1이 출력되지?

$ false || echo "Oops fail" # 어느 한 명령문이라도 만족하면 실행
Oops fail 

$ true || echo "oops fail" # [?] 이건 왜 출력이 안되지
$ true && echo "Things went well"
Things went well

$ false ; echo "This always prints"
This always prints
```

- `$(X)`: 파이썬의 string formatting과 유사

```shell
$ echo "We are in $(pwd)"
We are in /mnt/c/Users/iloveslowfood
```

- `<(X)`: [?] 뭔지 잘 모르겠다

```shell
$ cat <(ls)
```

- `?`

```
$ mkdir foo1
$ mkdir foo2
$ ls foo? # foo 이름을 지닌 디렉토리에 대해 list up
foo1:

foo2:
```

- `convert`

```shell
$ convert img.png img.jpg
$ convert img.{png, jpg} img.jpg
```

- `touch`: 파일의 날짜 시간 정보를 변경하는 명령어

```shell
$ touch newfile # 빈 파일 생성
$ touch -c newfile # newfile의 시간정보를 현재 시간으로 변경
$ touch -t 20210207 newfile # newfile의 시간정보 변경(YYYYMMDDhhmm)
$ touch -r oldfile newfile # newfile의 시간정보를 oldfile과 같게 변경
```

- convention

```shell
$ touch {foo, bar}/{a..j} # fooa, foob, ..., fooj, bara, ..., barj
```

- tldr package
- 파일/폴더 잘 찾아보기

```shell
$ find . -name src -type d # 이름이 src이고 타입이 directory인 데이터 모두 찾기
$ find . -path '**/test/*.py' -typ f
$ find / -mtime -1 # 1일 전에 수정한 데이터 모두 찾기
```

- `locate`

```shell
$ locate missing-semester # 조건에 맞는 디렉토리를 출력
```

- `rg`

```shell
$ rg 'import requests' -t py ~/scratch # 디렉토리 내 import requests가 등장한 인덱스 출력 
$ rg -u 'import requests' -t py ~/scratch # -u: 숨김파일을 무시하지 않음
```

- `fzf`: interactive하게 명령어를 수행할 수 있음

- `broot`
- `nnn`

> Reference

- [Lecture 2: Shell Tools and Scripting (2020)](https://www.youtube.com/watch?v=kgII-YWo3Zw&list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J&index=2)



> Attitude & Tips

- 영상의 24:28 부분을 한번 더 봐야 될듯(shebang ?)