def simulate_fifo(page_references, frames):
    page_table = []  # Page table to keep track of pages in memory
    page_faults = 0  # Counter for page faults

    for page in page_references:  # Iterate through each page in the page references
        if page in page_table:  # If page is already in memory, continue to next page
            continue  # Continue to the next page
        
        else:  # If page is not in memory
            if len(page_table) == frames:  # Check if the page table is full
                page_table.pop(0)  # Remove the oldest page from the page table
            
            page_table.append(page)  # Add the current page to the page table
            page_faults += 1  # Increment page fault counter

    return page_faults  # Return the total number of page faults
