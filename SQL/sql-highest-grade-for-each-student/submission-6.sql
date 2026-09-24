-- Write your query below
with exams_ranked as (
    select student_id, exam_id, score,
    ROW_NUMBER() OVER (
        PARTITION BY student_id
        ORDER BY score DESC, 
        exam_id ASC
    ) as ranking
    from exam_results
) SELECT student_id, exam_id, score 
FROM exams_ranked 
WHERE ranking = 1;