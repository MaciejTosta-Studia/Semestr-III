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

    while len(processes_done) < len(processes_copy):
        if processes_queue:
            process = processes_queue[0]
            time_delta = min(process['burst_time'], quantum)
            current_time += time_delta
            process['burst_time'] -= time_delta

            while processes and processes[0]["arrival_time"] <= current_time: processes_queue.append(processes.popleft())
            if len(processes_queue) > 1: context_switches += 1
            responded_times[process["process_id"]], process["responded"] = (current_time - process["arrival_time"], True) if not process["responded"] else (responded_times[process["process_id"]], process["responded"])    

            if process['burst_time'] == 0:
                turnaround_times[process['process_id']] = current_time - process['arrival_time']
                waiting_times[process['process_id']] = turnaround_times[process['process_id']] - processes_copy[process['process_id']]['burst_time']
                processes_done.append(processes_queue.popleft())
            else:
                processes_queue.rotate(-1)
        else:
            current_time = processes[0]["arrival_time"]
            processes_queue.append(processes.popleft())

    result = [{"process_id": x, 
             "turnaround_time": turnaround_times[x], 
             "responded_time": responded_times[x],
             "waiting_time": waiting_times[x]} for x in range(len(waiting_times))]

    return result, sum([x["burst_time"] for x in processes_original])/current_time