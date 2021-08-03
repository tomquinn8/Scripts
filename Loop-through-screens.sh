for i in  $(screen -ls | grep Detached | cut -d. -f2 | awk '{print $1}'); do screen -r $i; done
