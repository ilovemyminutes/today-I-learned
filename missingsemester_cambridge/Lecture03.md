# Lecture 3. Editors(vim)

VIM: 다양한 프로그래머들이 사용하는 에디터

- 입문하기는 쉽지만, 마스터하기에는 평생 시간이 걸릴 지도 모름
- GUI 기반의 에디터 중 가장 선호하는 에디터는 VSCode, 커맨드라인 기반 에디터 중 가장 선호하는 에디터는 VIM
- 본 수업에서는 VIM의 방대한 모든 것을 배우는 것이 아닌, 핵심 철학에 기반한 기본적인 것들을 배움
- 대부분의 시스템에서는 pre-installed되어 있음
- 마우스는 NO! 오로지 키보드만 활용해 불필요한 시간을 줄일 수 있음
- *VIM is modal editor*: multiple operating mode 지원
- VIM 자체로 프로그래밍 언어
- (무거운) 에디터를 별도로 실행하지 않고 코드를 작성할 수 있다는 장점
  - 가령, Python Extension이 설치된 VSCode를 실행하여 파이썬 파일을 수정하지 않고, VIM으로 바로 접근하여 수정하는 경우

Mode

- Normal mode

  - VIM의 기본적인 모드
  - 파일 탐색 등 내비게이팅에 활용
  - 모든 키 입력이 한 가지 방식으로 동작
  - [?] 사소한 수정을 할 수 있음
  - `h`, `j`, `k`, `l`: 상하좌우 커서 이동
    - `j`: 아래로 이동
    - `8 + j`: 8칸 만큼 아래로 이동
  - `w`: 단어 단위 커서 이동(단어: 공백 기준)
  - `e`: 단어의 마지막 문자로 커서 이동
  - `0`: 해당 라인의 맨 앞으로 커서 이동
  - `$`: 해당 라인의 맨 뒤로 커서 이동
  - `^`: 해당 라인의 문자가 처음 등장한 위치로 커서 이동
  - `Crtl + u/d`: 10줄 위/아래로 커서 이동
  - `G`: 최상단으로 커서 이동
  - `gg`: 최하단으로 커서 이동
  - `l`: 보이는 커맨드 라인 중 최하단으로 커서 이동
  - `m`: 보이는 커맨드 라인 중 중간으로 커서 이동
  - `h`:보이는 커맨드 라인 중 최상단으로 커서 이동
  - `f + 알파벳`: 커서 이후 내용 중 해당 문자로 시작하는 가장 가까운 단어로 커서 이동
  - `F + 알파벳`: 커서 이전 내용 중 해당 문자로 시작하는 가장 가까운 단어로 커서 이동
  - [?] `t`: to
  - `d`: delete, `d` 와 다른 명령어를 혼합하여 사용
    - `d + w`: 커서가 위치한 단어를 제거
    - `d + d`: 커서가 위치한 라인을 제거
    - `7 + d + w`: 커서의 뒤 7개 단어를 제거  
    - `d + i + (`: `(` 브래킷 내부 내용을 제거한 뒤 insert mode로 접근
    - `d + a + `: `(` 브래킷과 브래킷 내부 내용을 제거
  - `u`: undo, 직전 실행 취소
  - `c`: change, 해당 내용을 다른 내용으로 변경
    - delete(`d`)와의 차이점: delete는 실행 후 Normal mode로 남아있고, change(`c`)는 실행 후 Insert mode에 접근
    - `c + e`: 커서가 위치한 단어의 마지막 글자를 다른 내용으로 변경
    - `c + c`: 커서가 위치한 라인을 제거하고 다른 내용으로 변경
    - `c + 2 + w`:  커서 이후 2개의 단어를 다른 내용으로 변경
    - `c + i + [`: `[` 브래킷 내부의 내용을 제거하고 수정
  - `%`: 커서를 브래킷 단위로 이동
  - `x`: 커서가 위치한 문자를 제거
  - `Ctrl + r`: Redo, 직전 실행을 반복
  - `y`:복사
    - `yy`: 커서가 위치한 라인을 복사
    - `yw`: 커서가 위치한 단어를 복사
  - `p`: 복사한 라인을 바로 아래에 붙여넣기
  - `o`: 해당 커서 바로 아래 새로운 라인을 만들고 insert mode 활성화 
  - `O`: 해당 커서 바로 위에 새로운 라인을 만들고 insert mode 활성화

- Insert mode

  - Normal mode에서 `i`키를 통해 접근

  - 파일 타이핑 등 입력을 텍스트 버퍼에 담을 수 있음

  - `<esc>`키를 통해 Normal mode로 돌아갈 수 있음

    ```shell
    $ vim sample.md
    ~                                                                                                             ~
    ~                                                                                                             -- INSERT --  # i 버튼을 통해 insert mode 
    ```

- Replace mode

  - `R`키를 통해 접근

- Visual mode

  - 블럭을 지정할 수 있음
  - `v`키를 통해 접근
    - Visual-line: `Shift + v`를 통해 접근
    - Visual-block: `Ctrl + v`를 통해 접근
  - `e`: 단어의 끝부분까지 블록킹

- Command-line mode

  - `:`키를 통해 접근

    ```shell
    $ vim sample.md
    ~                                                                                                             ~
    ~                                                                                                             :  # : 버튼을 통해 command-line mode 
    :q # 파일로부터 나가기
    :wq # 파일의 수정 내용을 덮어쓴 뒤 나가기
    ```

    - `:q`는 현재 창을 닫는 것이지, 엄밀하게는 종료하는 것과 다른 개념

  - `help`: 명령어 매뉴얼 조회

    ```
    $ vim sample.md
    ~                                                                                                             ~
    ~                                                                                                             :help :w
    4. Writing                                      writing save-file
    
    Note: When the 'write' option is off, you are not able to write any file.
    
                                                            :w :write
                                            E502 E503 E504 E505
                                            E512 E514 E667 E796 E949
    :w[rite] [++opt]        Write the whole buffer to the current file.  This is
    ...
    ```

  - `sp`: 파일을 두 창으로 분리해 조회할 수 있음

    - 같은 파일의 다른 부분을 동시에 보고자 할 때 활용
    - 여러 번 실행하면 여러 개의 스플릿뷰 가능

    ```shell
    insert modesdfasdfasdfsdfasdf
    update something new
    ~                                                                                                             ~                                                                                                             ~                                                                                                             ~                                                                                                             sample.md                                                               2,20           All
    insert modesdfasdfasdfsdfasdf
    update something new
    ~
    ~
    ~
    ~                                                                                                             
    ```

    

> Attitude & Tips

[?] Emulation Mode

[?]`:tabnew`

[?] muscle memory - 뭔가 VIM이 가장 날 것에 가까운 코딩이 가능해서 너가 기대하는 속도를 내줄 것이라는 식으로 말한 것 같은데..

[?] HJKL

[?] `.`, `..` <- 영상의 44분 8초에 등장하는 커맨드