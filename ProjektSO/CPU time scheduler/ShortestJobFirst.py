from collections import deque

class sjf_scheduler():
    def __init__(self, original_processes):

        self.original_processes = original_processes
        self.processes = deque(sorted(original_processes, key=lambda x: x['arrival_time']))

        self.current_time = self.processes[0]['arrival_time']
        self.is_sorted = False

        self.turnaround_time = [0] * len(self.processes)
        self.waiting_time = [0] * len(self.processes)

        self.processes_queue = deque([self.processes.popleft()])
        self.processes_done = []

    def add_processes_to_queue(self):
        if self.processes:
            while self.processes and self.processes[0]['arrival_time'] <= self.current_time:
                self.processes_queue.append(self.processes.popleft())
        if not self.processes_queue:
            self.current_time = self.processes[0]['arrival_time']
            self.processes_queue.append(self.processes.popleft())

    def new_process(self):
        if self.processes and not self.is_sorted:
            process = min(self.processes_queue, key=lambda x: x['burst_time'])
            while process != self.processes_queue[0]:
                self.processes_queue.rotate(-1)
        elif not self.is_sorted:
            self.processes_queue = deque(sorted(list(self.processes_queue), key=lambda x: x['burst_time']))
            process = self.processes_queue[0]
            self.is_sorted = True
        else:
            process = self.processes_queue[0]

        return process
    
    def execute_process(self, process):
        self.current_time += process['burst_time']
        self.turnaround_time[process["process_id"]] = (self.current_time - process['arrival_time'])
        self.waiting_time[process["process_id"]] = (self.turnaround_time[process["process_id"]] - process['burst_time'])
        self.processes_done.append(self.processes_queue.popleft())

    def execute(self):
        while len(self.processes_done) < len(self.original_processes):
            self.add_processes_to_queue()
            process = self.new_process()
            self.execute_process(process)
        return [{"process_id": x,
                 "turnaround_time": self.turnaround_time[x],
                 "waiting_time": self.waiting_time[x]} for x in range(len(self.waiting_time))]
    

