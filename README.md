# art_archive

## Project 1
----
#### 3. 다음 작업을 수행하는 SQL query들과 해당 리턴 값을 작성해주시기 바랍니다. [풀이](https://github.com/paulsoh/art_archive/blob/master/sections/section3.md)

#### 4. CRUD 를 간략하게 설명해주세요

  > CRUD는 create, read, update, delete 의 앞글자를 따서 만든 줄임말로, *기억장치*에서 사용되는 가장 기본적인 기능들이다.

  > 기억 장치에 신규 entity를 추가하는 기능을 create,
  > 수정하는 기능을 update,
  > 삭제하는 기능을 delete,
  > 그리고 저장되어있는 값을 읽는 기능을 read라고 한다.

  > 데이터 베이스(MySQL) 관점에서 CRUD는 각각 INSERT, SELECT, UPDATE, DELETE과 대응되는 개념이라고 볼 수 있다.

#### 5. art_archive 데이터를 활용한 CRUD 기반의 REST API를 설계하시고 이 API를 활용할 다른 엔지니어들이 이해할 수 있는 Documentation 을 만들어주세요. [풀이](https://github.com/paulsoh/art_archive/blob/master/sections/section5/section5.md)

#### 6. TDD 를 설명해주세요. 이 개발 방식의 장단점은 무엇일까요? [풀이](https://github.com/paulsoh/art_archive/blob/master/sections/section6.md)

## Project 2. API 기능 구현하기
----
1. 개발 환경
    * Python 3.5.1
    * 사용한 Python 패키지: Flask 외 다수 (requiremest.txt 참조)
2. 개발 환경 맞추기
    1. 가상 환경 생성 및 구동(Python 3.5.1)
      ```
      $ pyenv virtualenv 3.5.1 art_archive
      $ pyenv activate art_archive
      $ (art_archive) $
      ```
    2. 개발 환경 동기화
      ```
      (art_archive) $ pip install -r requirements.txt
      ```
    3. 서버 구동
      ```
      (art_archive) $ python art_archive_project/run.py
      ```
      ```
      * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
      * Restarting with stat
      * Debugger is active!
      * Debugger pin code: 223-649-643
      ```

    4. 단위 테스트 Suite 실행 
      ```
      (art_archive) $ ./test.sh
      ```
