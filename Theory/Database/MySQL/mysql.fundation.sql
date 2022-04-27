#모든 데이베이스 목록 보기
SHOW DATABASES;
#데이터베이스 만들기
CREATE DATABASE mydatabase;
#사용할 데이터베이스 지정하기
USE mydatabase;
#테이블 만들기
CREATE TABLE mytable(
        col1 INT,
        col2 CHAR(2)
);
#테이블에 데이터 삽입하기
INSERT INTO mytable(col1, col2)
VALUES (1,'a'), (2,'b'), (3,'c'), (4,'d'), (5,'e');
#모든 데이터 가져오기
SELECT * FROM mytable;

/*
1 여러 줄 메모 처리
2
3
*/
