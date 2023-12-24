def all_partitions(input_set): 
    partitions = []

    def partition_helper(remaining, current_partition):
        if not remaining:
            print(current_partition)
            partitions.append(current_partition)
            return
        element = remaining.pop()
        
        # Include the element in the current partition
        partition_helper(remaining.copy(), current_partition + [element])
        # Exclude the element from the current partition
        partition_helper(remaining.copy(), current_partition)

    partition_helper(input_set.copy(), [])
    return partitions

A = []
while True:
    element = input("Enter an element (or press Enter to finish): ")
    if not element:
        break
    A.append(element)
result = all_partitions(A)
