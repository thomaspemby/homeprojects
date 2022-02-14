sampleArray = [2,41,1,45,4,0,12,2]

def bubble_sort(our_list):
    has_swapped = True

    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations - 1):
            if our_list[i] > our_list[i+1]:
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
        num_of_iterations += 1
    print("\nThe sorted array after {} steps: {}".format(num_of_iterations, str(our_list)))

bubble_sort(sampleArray)