-- Write your query below
select e1.student_id, e1.exam_id, e1.score from exam_results e1
    WHERE NOT EXISTS (
    SELECT 1 FROM exam_results e2 where e1.student_id = e2.student_id and
    (e1.score < e2.score or (e1.score = e2.score and e1.exam_id > e2.exam_id))
    )
order by e1.student_id asc;