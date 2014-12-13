 mysql -u pymorph -ppymorph Santa -e "select * from toys where duration between 2.5*60  and 24*60 order by duration desc;" > good_jobs.csv
mysql -u pymorph -ppymorph Santa -e "select * from toys where duration > 24*60 order by duration desc;" > big_jobs.csv

 mysql -u pymorph -ppymorph Santa -e "select * from toys where duration < 2.5*60 order by duration desc;" > tiny_jobs.csv
