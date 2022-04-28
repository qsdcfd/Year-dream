DROP DATABASE IF EXISTS pokemon;
CREATE DATABASE pokemon;
USE pokemon;
CREATE TABLE mypokemon (
			number int,
            name varchar(20),
            type varchar(20),
            height float,
            weight float,
            attack float,
            defense float,
            speed float
            );
INSERT INTO mypokemon (number, name, type, height, weight, attack, defense, speed)
VALUES (10, 'caterpie', 'bug', 0.3, 2.9, 30, 35, 45),
		(25, 'pikachu', 'electric', 0.4, 6, 55, 40, 90),
		 (26, 'raichu', 'electric', 0.8, 30, 90, 55, 110),
		 (133, 'eevee', 'normal', 0.3, 6.5, 55, 50, 55),
		 (152, 'chikoirita', 'grass', 0.9, 6.4, 49, 65, 45);

# ---
/*
MISSION (1)
포켓몬 테이블에서 포켓몬들의 이름과 키, 몸무게를 가져와 주세요.
*/

SELECT name, height, weight
FROM mypokemon;

/*
MISSION (2)
포켓몬 테이블에서 포켓몬들의 이름과 공격력, 방어력, 속도를 가져와 주세요.
*/

SELECT name, attack, defense, speed
FROM mypokemon;

/*
MISSION (3)
포켓몬 테이블에서 포켓몬들의 이름과 능력치의 합을 가져와 주세요.
조건 1. 능력치의 합은 공격력, 방어력, 속도의 합을 의미합니다.
조건 2. 능력치의 합은 ‘total’이라는 별명으로 가져와 주세요.
힌트. 숫자형 데이터 타입 컬럼 간에는 연산이 가능합니다.
*/

SELECT name, attack + defense + speed AS total
FROM mypokemon;
