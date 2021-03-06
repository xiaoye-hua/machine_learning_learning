## Question 1.2
ep_len = 1000
eval_batch_size=5000, namely epoch=5


|Task|Mean return (BC)|STD (BC)|Mean return (expert)|STD (expert)|
|---|---|---|---|---|
|Ant-v2|1252.3|301.48|4741.17|124.06|
|HalfCheetah-v2|2946.96|121.80|4140.33|96.49|

## Question 1.3
HalfCheetah-v2

eval_batch_size/ep_len (1, 5, 10, 15, 30, 60, 100) --> no relation to performance:
1. average_return: 2725, 2946.96, 2909.89, 2930, 2959, 2983.09, 2980
2. std_return: 0, 121, 186, 182, 210, 189, 176

--num_agent_train_steps_per_iter(affect training epoches) (1000, 2000, 5000, 10000, 50000):
1. average_return: 2946, 3708, 3993.39, 4083, 4100.84
2. std_return: 121.8, 156, 95.99, 52.49, 81

## Question 2.2
HalfCheetah-v2

iteration (1-5):
1. average_return: 2946, 3755, 3944, 4077, 4148, 
2. std_return: 121, 100, 132, 28, 113, 
