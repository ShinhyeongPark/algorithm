WITH RECURSIVE time AS(
    SELECT 0 AS hour
    UNION ALL
    SELECT hour+1 FROM time WHERE hour <23
)
SELECT hour, COUNT(ANIMAL_ID) as COUNT
FROM TIME
LEFT OUTER JOIN ANIMAL_OUTS 
on (hour = date_format(DATETIME, '%H'))
GROUP BY hour
ORDER BY HOUR

-- WITH RECURSIVE 테이블 : 가상의 테이블 생성

-- 중성화 된지 확인하는 방법은 IN과 OUT이 다르면 바뀐것
-- 너무 어렵게 생각..
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_OUTS AS O
LEFT OUTER JOIN ANIMAL_INS AS I
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE O.SEX_UPON_OUTCOME != I.SEX_UPON_INTAKE
ORDER BY ANIMAL_ID
