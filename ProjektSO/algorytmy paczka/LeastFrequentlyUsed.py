def simulate_lfu(page_references, frames):
    page_table = []  # Initialize an empty page table
    page_faults = 0  # Initialize the page fault counter
    page_counts = {}  # Initialize a dictionary to keep track of page counts

    for page in page_references:  # Iterate through each page in the page references
        if page in page_table:  # Check if the page is already in the page table
            page_counts[page] = page_counts.get(page, 0) + 1  # Increment the count of the current page
            continue    # Continue to the next page
        
        else:  # Check if the page is not in the page table
            if len(page_table) == frames:  # Check if the page table is full
                least_frequently_used = min(page_table, key=page_counts.get)  # Find the least frequently used page in the page table
                
                del page_counts[page_table.pop(page_table.index(least_frequently_used))]  # Remove the least frequently used page from the page table and remove its counter from the page counts dictionary
            page_table.append(page)  # Add the new page to the page table
            page_faults += 1  # Increment the page fault counter
            page_counts[page] = 1 # Add the new page to the page counts dictionary

    return page_faults  # Return the total number of page faults
