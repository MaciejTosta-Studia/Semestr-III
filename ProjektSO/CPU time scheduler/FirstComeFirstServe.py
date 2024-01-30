from collections import deque

def fcfs_scheduler(original_processes):
    # Sort the processes based on arrival time
    processes = deque(sorted(original_processes, key=lambda x: x['arrival_time']))

    # Initialize waiting time and turnaround time arrays
    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    
    # Set the current time to the arrival time of the first process
    current_time = processes[0]["arrival_time"]
    context_switches = 0

    # Process the tasks until all processes are done
    while processes:
        # Get the next process from the queue
        process = processes.popleft()

        # If the current time is less than the arrival time of the process,
        # update the current time to the arrival time of the process
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']

        # Update the current time by adding the burst time of the process
        current_time += process['burst_time']

        # Calculate the turnaround time and waiting time for the process
        turnaround_time[process['process_id']] = (current_time - process['arrival_time'])
        waiting_time[process['process_id']] = turnaround_time[process['process_id']] - process['burst_time']

    # Create a list of dictionaries representing the result
    result = [{"process_id": x,
                "turnaround_time": turnaround_time[x],
                "waiting_time": waiting_time[x]} for x in range(len(waiting_time))]

    return result

# Solution by Maciej Tośta
