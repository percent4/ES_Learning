TIMES=5
for i in $(eval echo "{1..$TIMES}")
do
    siege -c 1 -r 10 http://localhost:5000/
    siege -c 1 -r 5 http://localhost:5000/io_task
    siege -c 1 -r 5 http://localhost:5000/cpu_task
    siege -c 1 -r 3 http://localhost:5000/random_sleep
    siege -c 1 -r 10 http://localhost:5000/random_status
    sleep 5
done
