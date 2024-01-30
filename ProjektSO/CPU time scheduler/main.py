from DataExporter import export_data
from FirstComeFirstServe import fcfs_scheduler
from DataGenerator import generate_processes
from LastComeFirstServe import lcfs_scheduler
from ShortestJobFirst import sjf_scheduler
from RoundRobin import rr_scheduler
from testy import sjf_scheduler as sjf_test
from Functions import smth
import numpy as np
from time import time



def main():
    path = r'C:\Users\user\Desktop\ProjektSO\CPU time scheduler\test7'
    processes = generate_processes(False, False, [0, 200, 1, 100], 1000000)
    quantum = int(np.mean([x["burst_time"] for x in processes]))


    print("====================================")
    #fcfs_result =fcfs_scheduler(processes)
    #lcfs_result = lcfs_scheduler(processes)
    #rr_result = rr_scheduler(processes, quantum)

    start = time()
    sjf_result = sjf_scheduler(processes)
    print(time() - start)
    start = time()
    sjf_test_result = sjf_test(processes)
    print(time() - start)
    start = time()
    smth_result = smth(processes).execute()
    print(time() - start)

    print(np.mean([x["waiting_time"] for x in sjf_result]))
    print(np.mean([x["waiting_time"] for x in sjf_test_result]))
    print(np.mean([x["waiting_time"] for x in smth_result]))
    
    #for x in sjf_test_result:
    #    print(x)

    #export_data(processes, path + '/data_set.csv')
    #export_data(fcfs_result, path + '/fcfs.csv')
    #export_data(lcfs_result, path + '/lcfs.csv')
    #export_data(sjf_result, path + '/sjf.csv')
    #export_data(rr_result[0], path + f'/rr_q{quantum}_cs{rr_result[1]}.csv')
     

if __name__ == "__main__":
    main()