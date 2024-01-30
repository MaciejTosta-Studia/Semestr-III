from copy import deepcopy
from collections import deque

def rr_scheduler(processes_original, quantum):
    processes_copy = deepcopy(sorted(processes_original, key=lambda x: x['process_id']))
    processes = deque(deepcopy(sorted(processes_original, key=lambda x: x['arrival_time'])))

    current_time = processes[0]['arrival_time']
    context_switches = 0

    waiting_times = [0]* len(processes)
    turnaround_times = [0]* len(processes)
    responded_times = [0]*len(processes)

    processes_queue = deque([processes.popleft()])
    processes_done = []

    # Process the tasks until all processes are done
    while len(processes_done) < len(processes_copy):
        if processes_queue:
            # Get the first process in the queue
            process = processes_queue[0]
            # Calculate the time delta
            time_delta = min(process['burst_time'], quantum)
            current_time += time_delta
            process['burst_time'] -= time_delta

            # Add processes to the queue that have arrived before or at the current time
            while processes and processes[0]["arrival_time"] <= current_time:
                processes_queue.append(processes.popleft())

            # Check if there are more than one process in the queue, indicating a context switch
            if len(processes_queue) > 1:
                context_switches += 1
            
            # Check if the process has already responded
            if process["responded"] == False:
                responded_times[process["process_id"]] = current_time - process['arrival_time']
                process["responded"] = True    

            # Check if the process has completed its burst time
            if process['burst_time'] == 0:
                turnaround_times[process['process_id']] = current_time - process['arrival_time']
                waiting_times[process['process_id']] = turnaround_times[process['process_id']] - processes_copy[process['process_id']]['burst_time']
                processes_done.append(processes_queue.popleft())
            else:
                # Rotate the queue to move the current process to the end
                processes_queue.rotate(-1)
        else:
            # If the queue is empty, set the current time to the arrival time of the next process
            current_time = processes[0]["arrival_time"]
            processes_queue.append(processes.popleft())

    # Create a list of dictionaries representing the scheduling results
    result = [{"process_id": x, 
             "turnaround_time": turnaround_times[x], 
             "responded_time": responded_times[x],
             "waiting_time": waiting_times[x]} for x in range(len(waiting_times))]

    return result, context_switches