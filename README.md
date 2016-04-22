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
