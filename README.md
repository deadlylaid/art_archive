# art_archive
 
#### 3. 다음 작업을 수행하는 SQL query들과 해당 리턴 값을 작성해주시기 바랍니다.

+ 제니 오델’라는 name을 가진 artist 의 image들의 title들을 가져오기
```
SELECT images.title FROM images
WHERE images.artist_id
IN
    (SELECT artists.id FROM artists
    WHERE artists.name = '제니 오델');
```

Return value

| title            |
|------------------|
| 쓰레기 셀카      |

`1 row in set (0.00 sec)`

+ 인상주의' artist 의 3개의 image들 가져오기
```
SELECT images.image_url, images.title, artists.name, images.year, images.description 
FROM images 
LEFT JOIN artists 
ON artists.id = images.artist_id
WHERE artists.genre = '인상주의'
LIMIT 3;
```

Return value(image_url는 테이블 공간 제약상 제외)

| title                      | name                | year | description         |
|----------------------------|---------------------|------|---------------------|
| 비눗방울 부는 소년         | 에두아르 마네       | 1867 | 캔버스에 유채       |
| 풀밭 위의 점심식사         | 에두아르 마네       | 1863 | 캔버스에 유채       |
| 시골 경마장                | 에드가 드가         | 1869 | 캔버스에 유채       |

`3 rows in set (0.00 sec)`

+ images 테이블에 새로운 image 추가하기 (query statement만)

> 가정 1: 추가하려는 image는 다음과 같은 field가 있다.: 
> > *(image_title, image_url, image_year, artist_name, image_description)*

> 가정 2: *artists* table에 이미 존재하는 화가에 대해서만 새로운 image를 추가할 수 있다.

> 사용 예: 
```
mysql> call add_image('베토벤 프리즈', 'http://i.telegraph.co.uk/multimedia/archive/03223/frieze_2_3223137b.jpg', 1902, '구스타프 클림트', '벽화');
```

*add_image procedure* 구현 내용:

```
mysql> delimiter //
mysql> CREATE PROCEDURE add_image(
    IN title VARCHAR(255), 
    IN url VARCHAR(255), 
    IN year INT(11), 
    IN artist_name VARCHAR(45), 
    IN description VARCHAR(255)
)
BEGIN
    SET @artist_id = (SELECT artists.id 
                        FROM artists 
                        WHERE artists.name=artist_name);
    INSERT INTO images (image_url, 
                        title, 
                        year, 
                        artist_id, 
                        description)
    VALUES (url, 
            title, 
            year, 
            @artist_id, 
            description);
END //
mysql> delimiter ;
```

```
mysql> call add_image('베토벤 프리즈', 'http://i.telegraph.co.uk/multimedia/archive/03223/frieze_2_3223137b.jpg', 1902, '구스타프 클림트', '벽화');
Query OK, 1 row affected (0.00 sec)
```

Return value

| id | image_url                                                               | title               | year | artist_id | description |
|----|-------------------------------------------------------------------------|---------------------|------|-----------|-------------|
| 68 | http://i.telegraph.co.uk/multimedia/archive/03223/frieze_2_3223137b.jpg | 베토벤 프리즈       | 1902 |       149 | 벽화        |


+ 가장 많은 image 들을 가진 artist 가져오기
```
SELECT *
FROM artists
WHERE artists.id 
IN 
    (SELECT images.artist_id
    FROM images 
    GROUP BY images.artist_id
    ORDER BY count(*) desc) 
LIMIT 1;
```

| id  | name                 | birth_year | death_year | country      | genre               |
|-----|----------------------|------------|------------|--------------|---------------------|
| 102 | 빈센트 반 고흐       |       1853 |       1890 | 네더란드     | 후기 인상주의       |

`1 row in set (0.01 sec)`

#### 4. CRUD 를 간략하게 설명해주세요
CRUD는 create, read, update, delete 의 앞글자를 따서 만든 줄임말로, '기억장치'에서 사용되는 가장 기본적인 기능들이다. 
기억 장치에 신규 entity를 추가하는 기능을 create, 
수정하는 기능을 update, 
삭제하는 기능을 delete, 
그리고 저장되어있는 값을 읽는 기능을 read라고 한다. 

데이터 베이스(MySQL) 관점에서 CRUD는 각각 INSERT, SELECT, UPDATE, DELETE과 대응되는 개념이라고 볼 수 있다.

#### 6. TDD 를 설명해주세요. 이 개발 방식의 장단점은 무엇일까요?
TDD는 Test driven development의 줄임말로, 시험 주도의 개발 과정을 제창하는 소프트웨어 개발 방법론 중 하나이다. 
TDD의 핵심 내용은 다음과 같이 나눌 수 있다.

+ 시험 우선의 개발(Test first development)
+ 리팩토링(Refactoring)

일반적으로 시험 우선의 개발이 선행된 후, 리팩토링 과정을 진행하는 방식으로 TDD 방법론을 수행한다.

구체적인 TDD 방법론을 단계별로 구분하면 다음과 같다.
> <시험 우선의 개발 영역>
  1. 부분 테스트 코드를 작성한다.
  2. 부분 테스트가 실패하는 것을 확인한다. (성공한다면 다시 1 단계로 돌아간다)
  3. 부분 테스트가 통과할 만큼만의 코드를 작성한다. 이 과정은 테스트가 통과할 떄 까지 반복한다.

> <리팩토링 영역>
  4. 부분 테스트가 성공하면 누적된 전체 테스트들에 대하여 통과하는지 확인한다. (실패한다면 다시 시험 우선의 개발 영역으로 돌아간다.)
  5. 전체 테스트가 통과하면 코드 리팩토링를 진행하며 진행 중에는 수시로 전체 테스트를 실시한다.
  6. 몇개의 시험이 지속적으로 실패한다면 테스트 내용을 업데이트 한다. 수정 후에는 다시 전체 테스트를 실시한다.

시험 우선의 개발에서는 부분 테스트에서 정의된 테스트 내용을 통과되게끔 코딩하는 것이 주 목적이고, 
리팩토링에서는 전체적인 코드의 레이아웃 및 디자인과의 합치되게끔 하는 것이 주 목적이다.

개인적으로 생각하는 TDD의 장점은 다음과 같다.
  + 추후 작성

개인적으로 생각하는 TDD의 단점은 다음과 같다.
  + 추후 작성
