-- Write your query below
select student_id, exam_id, score from exam_results
where (exam_id, student_id) NOT IN (
    select e1.exam_id, e1.student_id from exam_results e1
    join exam_results e2 on e1.student_id = e2.student_id
    where e1.score < e2.score or (e1.score = e2.score and e1.exam_id > e2.exam_id)
) order by student_id asc;