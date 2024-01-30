from collections import deque
import warnings

def fcfs_scheduler(original_processes):
    processes = deque(sorted(original_processes, key=lambda x: x['arrival_time']))

    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    
    current_time = processes[0]["arrival_time"]
    context_switches = 0

    while processes:
        process = processes.popleft()

        if current_time < process['arrival_time']:
            current_time = process['arrival_time']

        current_time += process['burst_time']
        turnaround_time[process['process_id']] = (current_time - process['arrival_time'])
        waiting_time[process['process_id']] = turnaround_time[process['process_id']] - process['burst_time']

    result = [{"process_id": x,
                "turnaround_time": turnaround_time[x],
                "waiting_time": waiting_time[x]} for x in range(len(waiting_time))]

    return result, sum([x["burst_time"] for x in original_processes])/current_time

#solution by Maciej Tośta
