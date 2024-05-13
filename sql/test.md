Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

```SQL
SELECT * 
FROM CITY
WHERE COUNTRYCODE = "USA" AND POPULATION > 100000
```

Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.


```SQL
SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0
```

Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

```SQL
SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION
```

Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

```SQL
(SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY), CITY
LIMIT 1
)
UNION ALL
(
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY
LIMIT 1
)
```

Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

```SQL
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU]';
```

Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

```SQL
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU].*[aeiouAEIOU]$';
```

Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

```SQL
select name from students
where marks > 75
order by right(name, 3), id
```


Query the smallest Northern Latitude (LAT_N) from STATION that is greater than . Round your answer to  decimal places.
```SQL
select round(min(LAT_N), 4) from station 
where LAT_N > 38.778
```

Calculate median
```SQL
select round(avg(LAT_N), 4)
from (select LAT_N,
    ROW_NUMBER() over (order by LAT_N asc) as RNAsc,
    ROW_NUMBER() over (order by LAT_N desc) as RNDesc
    from station
) as x
where x.RNAsc in (x.RNDesc, x.RNDesc + 1, x.RNDesc - 1)
```

The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  from your result.

```SQL
select 
hackers.hacker_id as hacker_id, 
hackers.name as name, 
sum(x.max_score) as total_score

from hackers

join

(select hacker_id, challenge_id, max(score) as max_score
from Submissions
group by hacker_id, challenge_id) x    

on hackers.hacker_id = x.hacker_id

group by hacker_id, name
HAVING total_score > 0

order by total_score desc, hacker_id
```

P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

* * * * * 
* * * * 
* * * 
* * 
*
Write a query to print the pattern P(20).

```SQL
SET  @number  =  21;
SELECT  REPEAT('* ',  @number :=  @number  -  1)
FROM information_schema.tables
WHERE  @number  >  0;
```


Write a query to print all prime numbers less than or equal to . Print your result on a single line, and use the ampersand () character as your separator (instead of a space).

```SQL
With recursive Seq(n) as 
(
    select 2
    union all
    select n + 1
    from Seq
    where n < 1000
)
select group_concat(n SEPARATOR '&') from Seq A
where not exists
(
    select 1 from Seq B where A.n % B.n = 0 AND B.n > 1 AND B.n < A.n
)
```

You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.
```SQL
select 
case 
    when grade < 8 then NULL 
    else Name 
end as name, Grade as grade, Marks as mark
from students
join Grades
on marks <= max_mark and marks >= min_mark
order by grade desc, name asc, mark asc
```

Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

```SQL
/*
Enter your query here.
*/ 

select hackers.hacker_id, hackers.name

from hackers

join submissions on hackers.hacker_id = submissions.hacker_id

join challenges on challenges.challenge_id = submissions.challenge_id

join difficulty on difficulty.difficulty_level = challenges.difficulty_level

where submissions.score = difficulty.score

group by hacker_id, name

having count(*) > 1

order by count(*) desc, hacker_id asc
```


Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.

```SQL
select id, age, coins_needed, power
from wands join wands_property using (code)
where
    coins_needed = (
        select min(coins_needed)
        from wands W2 join wands_property WP2 using (code)
        where is_evil = 0 
        and W2.power = wands.power 
        and WP2.age = wands_property.age
    )
order by power desc, age desc

-- this is MSSQL version. MySQL might be different
with cte as (
    select id, code, coins_needed, power, age
    rank() over (partition by age, power order by coins_needed) as ranking
    from wands join wands_property using (code)
    where is_evil = 0
)

select id, age, coins_needed, power
from cte
where ranking = 1
order by power desc, age desc
```

Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. Exclude the contest from the result if all four sums are .

```SQL
SELECT con.contest_id, con.hacker_id, con.name,
SUM(sg.total_submissions), SUM(sg.total_accepted_submissions),
SUM(vg.total_views), SUM(vg.total_unique_views)
FROM Contests AS con
JOIN Colleges AS col ON con.contest_id = col.contest_id
JOIN Challenges AS cha ON cha.college_id = col.college_id
LEFT JOIN
(SELECT ss.challenge_id, SUM(ss.total_submissions) AS total_submissions, SUM(ss.total_accepted_submissions) AS total_accepted_submissions FROM Submission_Stats AS ss GROUP BY ss.challenge_id) AS sg
ON cha.challenge_id = sg.challenge_id
LEFT JOIN
(SELECT vs.challenge_id, SUM(vs.total_views) AS total_views, SUM(vs.total_unique_views) AS total_unique_views
FROM View_Stats AS vs GROUP BY vs.challenge_id) AS vg
ON cha.challenge_id = vg.challenge_id
GROUP BY con.contest_id, con.hacker_id, con.name
HAVING SUM(sg.total_submissions) +
       SUM(sg.total_accepted_submissions) +
       SUM(vg.total_views) +
       SUM(vg.total_unique_views) > 0
ORDER BY con.contest_id;

```