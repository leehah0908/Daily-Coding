select O.ANIMAL_ID, O.NAME
from ANIMAL_OUTS O left join ANIMAL_INS I on O.ANIMAL_ID = I.ANIMAL_ID
where I.ANIMAL_ID is null
order by ANIMAL_ID