#모든 레코드 조회
SELECT ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE FROM ANIMAL_INS ORDER BY ANIMAL_ID

#역순정렬
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;

#아픈동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'Sick' ORDER BY ANIMAL_ID;

#어린동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged' ORDER BY ANIMAL_ID

#동물 데이터 조회
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID;
