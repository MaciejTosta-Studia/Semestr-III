from LeastFrequentlyUsed import simulate_lfu
from MostFrequentlyUsed import simulate_mfu
from FirstInFirstOut import simulate_fifo
from LeastRecentlyUsed import simulate_lru
import DataExporter
from random import randint


def main():
    path = r"C:\Users\user\Desktop\ProjektSO\Page replacment algorithm\test9"
    page_references = [i % 5 + 1 for i in range(400)]
    fifo_results = []
    mfu_results = []
    lfu_results = []
    lru_results = []
    
    print(simulate_fifo(page_references, 4))
    print(simulate_mfu(page_references, 4))
    print(simulate_lfu(page_references, 4))
    print(simulate_lru(page_references, 4))

    for frames in range(3, 11):
        fifo_results.append([frames, simulate_fifo(page_references, frames)])
        mfu_results.append([frames, simulate_mfu(page_references, frames)])
        lfu_results.append([frames, simulate_lfu(page_references, frames)])
        lru_results.append([frames, simulate_lru(page_references, frames)])

    DataExporter.result_exporter(fifo_results, path+r"\fifo_results.csv")
    DataExporter.result_exporter(mfu_results, path+r"\mfu_results.csv")
    DataExporter.result_exporter(lfu_results, path+r"\lfu_results.csv")
    DataExporter.result_exporter(lru_results, path+r"\lru_results.csv")
    DataExporter.input_exporter(page_references, path+r"\input.csv")



if __name__ == "__main__":
    main()