def simulate_lru(page_references, frames):
    page_table = []  # Represents the page table
    page_faults = 0  # Keeps track of the number of page faults

    for page in page_references:  # Iterate over each page in the page references
        if page in page_table:  # If the page is already in the page table
            page_table.append(page_table.pop(page_table.index(page)))  # Move the page to the end of the page table
            continue  # Continue to the next page
        
        else:  # If the page is not in the page table
            if len(page_table) == frames:  # Check if the page table is full
                page_table.pop(0)  # Remove the least recently used page from the page table
            
            page_table.append(page)  # Add the current page to the page table
            page_faults += 1  # Increment the page fault counter

    return page_faults  # Return the total number of page faults