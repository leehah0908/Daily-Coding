-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
from ANIMAL_INS I left join ANIMAL_OUTS O using(ANIMAL_ID)
where O.SEX_UPON_OUTCOME regexp 'Spayed|Neutered'
and I.SEX_UPON_INTAKE like "Intact%" 
order by ANIMAL_ID