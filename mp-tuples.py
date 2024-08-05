#############################################
# Multiprocessing tuples example            #
# https://vicsprotips.com                   # 
# Vic Baker                                 #
#############################################

import multiprocessing

def doWork(params):
    """
    Each item from the queue will be processed here

    """
    try:
        number = params[0]
        letter = params[1]
        print(f"doWork is processing: {params}, number = {number}, letter = {letter}")
        return f"{number}-{letter}"
    except Exception as e:
        return f"Error processing {params}: {e}"

if __name__ == '__main__':

    # define a list of tuples
    numbers  = [1, 2, 3, 4, 5]
    letters  = ['a', 'b', 'c', 'd', 'e']

    queue = list(zip(numbers, letters))
    print(queue)
    print("Queue created.  Starting pool")
    
    pool = multiprocessing.Pool(3) # defining how many cores to use, blank defaults to all available
    results = pool.map(doWork, queue)
    pool.close()

    print("Pool done!  Printing results:")
    for r in results:
        print(r)
    