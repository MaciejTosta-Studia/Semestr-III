import numpy as np

def generate_processes(is_arrival_mean, is_burst_mean, args, task_count):
    if is_arrival_mean:
        arrival_time = np.random.normal(loc=args[0], scale=args[1], size=task_count)
        arrival_time = np.maximum(0, arrival_time)
    else: 
        arrival_time = np.random.randint(low=args[0], high=args[1], size=task_count)

    if is_burst_mean:
        burst_time = np.random.normal(loc=args[2], scale=args[3], size=task_count)
        burst_time = np.maximum(0, burst_time)
    else:
        burst_time = np.random.randint(low=args[2], high=args[3], size=task_count)
    
    return [{"process_id": i, "arrival_time": arrival_time[i], "burst_time": burst_time[i], "responded": False} for i in range(task_count)]
