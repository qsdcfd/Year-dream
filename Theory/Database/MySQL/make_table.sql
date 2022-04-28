#테이블 만든 후 데이터 넣기 실습
#포켓몬 데이터베이스 만든 후 포켓몬 테이블을 만들어서 데이터 넣기
SHOW DATABASES;
#데이터베이스 만들기
CREATE DATABASE pokemon;
#사용할 데이터베이스 지정하기
USE pokemon;

#테이블 만들기
CREATE TABLE mypokemon(
        number INT,
        name VARCHAR(20),
        type VARCHAR(10)
);
#테이블에 데이터 삽입하기
INSERT INTO mypokemon(number, name, type)
VALUES (10,'caterpie','bug'),
	   (25,'pikachu','electric'),
       (133,'eevee','normal');
#모든 데이터 가져오기
SELECT * FROM mypokemon;