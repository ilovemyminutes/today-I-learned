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

- `? `

```
$ mkdir foo1
$ mkdir foo2
$ ls foo? # foo 이름을 지닌 디렉토리에 대해 list up(물음표 하나당 한글자)
foo1:

foo2:
```

- `convert`

```shell
$ convert img.png img.jpg
$ convert img.{png, jpg} img.jpg
```

- `touch`: 파일 생성 또는 파일의 날짜 시간 정보를 변경하는 명령어

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

`diff`

```shell
$ diff <(ls foo) <(ls bar) # 디렉토리별 차이를 볼 수 있음(어떤 파일이 있고 없고)
4d3
< d
7a7,9
> h
> i
> j
```

**shebang**

- sharp(#) + bang(!)의 합성어 

- Unix계열 OS(리눅스, Mac)에서 스크립트(bash, python등등) **코드 최상단에서 해당 파일을 해석해줄 인터프리터의 절대경로 지정**

  ```shell
  #!/usr/bin/env python
  import sys
  for arg in reversed(sys.argv[1:]):
  	print(arg)
  ```

  

`tldr`

- 명령어의 사용법을 알기 편함

  ```shell
  $ tldr convert
  convert
  Imagemagick image conversion tool.More information: https://imagemagick.org/script/convert.php.
  
   - Convert an image from JPG to PNG:
     convert {{image.jpg}} {{image.png}}
  
   - Scale an image 50% its original size:
     convert {{image.png}} -resize 50% {{image2.png}}
  
   - Scale an image keeping the original aspect ratio to a maximum dimension of 640x480:
     convert {{image.png}} -resize 640x480 {{image2.png}}
  
   - Horizontally append images:
     convert {{image1.png}} {{image2.png}} {{image3.png}} +append {{image123.png}}
  
   - Vertically append images:
     convert {{image1.png}} {{image2.png}} {{image3.png}} -append {{image123.png}}
  
   - Create a gif from a series of images with 100ms delay between them:
     convert {{image1.png}} {{image2.png}} {{image3.png}} -delay {{10}} {{animation.gif}}
  
   - Create an image with nothing but a solid background:
     convert -size {{800x600}} "xc:{{#ff0000}}" {{image.png}}
  ```

  

- 파일/폴더 잘 찾아보기

```shell
$ find . -name src -type d # 이름이 src이고 타입이 directory인 데이터 모두 찾기
$ find . -path '**/test/*.py' -typ f
$ find / -mtime -1 # 1일 전에 수정한 데이터 모두 찾기
```

`locate`

```shell
$ locate missing-semester # 조건에 맞는 디렉토리를 출력
```

`rg`

```shell
$ rg 'import requests' -t py ~/scratch # 디렉토리 내 import requests가 등장한 인덱스 출력 
$ rg -u 'import requests' -t py ~/scratch # -u: 숨김파일을 무시하지 않음
```

`history`: 지난 실행 기록을 볼 수 있음

```shell
$ history
 1  sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
 2  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
 3  echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>! ~/.zshrc
 4  p10k configure
 5
 6  exec $SHELL
 7  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
 8  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    ...
```



- `fzf`: interactive하게 명령어를 수행할 수 있음
- `broot`
- `nnn`

> Reference

- [Lecture 2: Shell Tools and Scripting (2020)](https://www.youtube.com/watch?v=kgII-YWo3Zw&list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J&index=2)



> Attitude & Tips

- 영상의 24:28 부분을 한번 더 봐야 될듯(shebang ?)