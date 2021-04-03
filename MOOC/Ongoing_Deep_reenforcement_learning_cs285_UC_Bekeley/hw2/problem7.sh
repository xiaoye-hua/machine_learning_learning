#bin/bash

B_ARRAY=(10000 30000 50000)
R_ARRAY=(0.005 0.01 0.02)

for b in "${B_ARRAY[@]}"
  do
#    echo bash
    for r in "${R_ARRAY[@]}"
      do
        echo $b;
        echo $r;
        CMD="python run_hw2_policy_gradient.py --env_name HalfCheetah-v2 --ep_len 150 --discount 0.95 -n 100 -l 2 -s 32 -b $b -lr $r --video_log_freq -1 --reward_to_go --nn_baseline --exp_name hc_b{$b}_lr{$r}_nnbaseline"
#        $CMD
        python cs285/scripts/run_hw2_policy_gradient.py --env_name HalfCheetah-v2 --ep_len 150 --discount 0.95 -n 100 -l 2 -s 32 -b $b -lr $r --video_log_freq -1 --reward_to_go --nn_baseline --exp_name hc_b{$b}_lr{$r}_nnbaseline
      done
  done


#DB_AWS_ZONE=('us-east-2a' 'us-west-1a' 'eu-central-1a')
#
#for zone in "${DB_AWS_ZONE[@]}"
#do
#  echo "Creating rds (DB) server in $zone, please wait ..."
##  aws rds create-db-instance \
##  --availability-zone "$zone"
##  --allocated-storage 20 --db-instance-class db.m1.small \
##  --db-instance-identifier test-instance \
##  --engine mariadb \
##  --master-username my_user_name \
##  --master-user-password my_password_here
#done




