/*
데이터 베이스 만드는 과정

SHOW DATABASES;
#데이터베이스 만들기
CREATE DATABASE idol;
#사용할 데이터베이스 지정하기
USE idol;
#테이블 만들기
CREATE TABLE idol(
       name VARCHAR(20),
       age INT,
       group VARCHAR(50)
);
#테이블 이름 변경하기

*/

/*
데이터 베이스 문법

테이블 이름 변경하기
ALTER TABLE [테이블 이름] RENAME [새로운 테이블 이름];
EX) ALTER TABLE costomor RENAME customers;

새로운 컬럼 추가하기
ALTER TABLE[테이블 이름] ADD COLUMN[컬럼 이름][데이터 타입];
EX) ALTER TABLE customers ADD COLUMN age INT;

기존 컬럼 타입 변경하기
ALTER TABLE[테이블 이름]MODIFY COLUMN[컬럼 이름][새로운 데이터 타입];
EX)ALTER TABLE customers MODIFY COLUMN age FLOAT;

기존 컬럼 이름과 타입 변경하기
ALTER TABLE[테이블 이름]
CHANGE COLUMN[컬럼 이름][새로운 컬럼 이름][새로운 데이터 타입];
EX)
ALTER TABLE customers
CHANGE COLUMN age new_age FLOAT;

컬럼 지우기
ALTER TABLE[테이블 이름] DROP COLUMN[컬럼 이름];
ALTER TABLE customers DROP COLUMN new_age;

데이베이스 지우기
DROP DATABASE[데이터베이스 이름];

테이블 지우기
DROP TABLE[테이블 이름];

테이블 값만 지우기
TRUNCATE TABLE[테이블 이름];

데이터베이스/테이블이 존재한다면 지우기
DROP DATABASE IF EXISTS[데이터베이스 이름];
DROP TABLE IF EXISTS[테이블 이름];

데이터 하나 삽입하기(두 개의 리스트 갯수는 일치해야한다)
INSERT INTO[테이블 이름]([컬럼1 이름],[컬럼2 이름],[컬럼3 이름])
VALUES([컬럼1 값],[컬럼2 값],[컬럼3 값]); #로우(행)

EX)
INSERT INTO idol(name,age,group)
VALUES("제니",27,"블랙핑크");

데이터 여러 개 삽입
로우만 증가시키면 되고 쉼표로 행부분 구분

데이터 삭제하기
DELETE FROM[테이블 이름]
WHERE[조건 값];

데이터 수정하기
UPDATA[테이블 이름]
SET[컬럼 이름]=[새 값]
WHERE[조건 값];

*/
