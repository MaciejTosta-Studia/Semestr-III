from collections import deque

def lcfs_scheduler(original_processes):
    # Sort the processes based on arrival time
    processes = deque(sorted(original_processes, key=lambda x: x['arrival_time']))

    current_time = processes[0]['arrival_time']
    context_switches = 0

    turnaround_time = [0] * len(processes)
    waiting_time = [0] * len(processes)

    processes_queue = deque([processes.popleft()])
    processes_done = []

    # Process the processes until all are done
    while len(processes_done) < len(original_processes):
        # Add processes to the queue that have arrived by the current time
        if processes:
            while processes and processes[0]['arrival_time'] <= current_time:
                processes_queue.append(processes.popleft())
            processes_queue = deque(sorted(list(processes_queue), key=lambda x: x['arrival_time'], reverse=True))

        if processes_queue:
            # Get the process with the highest arrival time from the queue
            process = processes_queue[0]
            current_time += process['burst_time']
            # Calculate turnaround time and waiting time for the process
            turnaround_time[process["process_id"]] = (current_time - process['arrival_time'])
            waiting_time[process["process_id"]] = (turnaround_time[process["process_id"]] - process['burst_time'])
            processes_done.append(processes_queue.popleft())
        else:
            # If the queue is empty, set the current time to the arrival time of the next process
            current_time = processes[0]['arrival_time']
            processes_queue.append(processes.popleft())

    # Create a list of dictionaries representing the result
    result = [{"process_id": x,
                "turnaround_time": turnaround_time[x],
                "waiting_time": waiting_time[x]} for x in range(len(waiting_time))]
    
    return result


#solution by Maciej Tośta