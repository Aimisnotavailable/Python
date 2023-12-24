import time
set_a = []
size = 0
partitioned_list = []
current_size = 1
inds_p = []
current_list = []
arr = []
inds_p = []
start_1 = 10

# 0 , 1 , 2 , 3
# (0,1) (0,2) (0,3) (1,2) (1,3) (2,3) 
# (0,1,2) (0,1,3) (0,2,3) (1,2,3)
# (0,1,2,3)

# 0 , 1 , 2 , 3, 4
# (0,1) (0,2) (0,3) (0,4) (1,2) (1,3) (1,4) (2,3) (2,4) (3,4) 
# (0,1,2) (0,1,3) (0,1,4) (0,2,3) (0,2,4) (0,3,4) (1,2,3) (1,2,4) (1,3,4) (2,3,4)
# (0,1,2,3) (0,1,2,4) (1,2,3) (1,3,4)
# (0,1,2,3,4)

def store_partitions(prev_elm,start,count):
    for i in range(start,len(arr[count])):
        prev_elm += set_a[arr[count][i]]
        if(count == len(arr)-1):
            partitioned_list.append(prev_elm)
        else:
            store_partitions(prev_elm,i,count+1)
        prev_elm = prev_elm[:-1]
        
def seperate_chunks(start,interval,count):
    if(interval == 1):
        for i in current_list:
            partitioned_list.append(set_a[i])
    elif(interval == len(set_a)):
        pre_elm = ""
        for i in current_list:
            pre_elm += set_a[i]
        partitioned_list.append(pre_elm)
    else:
        if(count < (len(current_list)/interval)+1):
            arr.append(current_list[start:interval*count])
            seperate_chunks(start + interval, interval, count+1)
        else:
            store_partitions("",0,0)
            arr.clear()
        
            
def determine_chunk_elements(current_size, maximum_size):
    size = len(set_a)
    size_l = size - (maximum_size - current_size)
    for i in range(current_size, size_l):
       current_list.append(i)
    if(current_size == maximum_size):
        interv = len(current_list)/(maximum_size+1)
        seperate_chunks(0,int(interv),1)
        current_list.clear()
   
def determine_elements_per_chunk(current_size , maximum_size, start):
    determine_chunk_elements(current_size, maximum_size)
    if(current_size < maximum_size):
        current_size+=1
        start_l = start+1
        determine_elements_per_chunk(current_size, maximum_size, start_l)

def fill_size():
    for i in range(0, len(set_a)):
        inds_p.append(i)

def main():
    set_size = input("Enter total number of elements: ")
    insert_elements(int(set_size))
    start = time.time()
    fill_size()
    for i in inds_p:
        determine_elements_per_chunk(0, i, i)
    print_partitions()
    end = time.time()
    print(end - start)

def print_partitions():
    start = -(len(set_a))
    for i in range(start, len(partitioned_list)+start):
        if(i == 0):
            continue
        print(partitioned_list[i])
    print(partitioned_list[0])
    
    print("TOTAL NUMBER OF PARTITION : ", len(partitioned_list))

def insert_elements(set_size):
    elm_count = 0
    while(elm_count < set_size):
        print("Enter element no. ", elm_count+1, end = " ")
        elm = input()
        set_a.append(elm)
        elm_count+=1

main()

