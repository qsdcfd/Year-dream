-- Finance department에 속한 사람 중에 salary가 70000이 ㄴㅁ는 사람 모두 출력
SELECT name,dept_name,salary
FROM instructor
WHERE dept_name = 'Finance' and salary > 70000;