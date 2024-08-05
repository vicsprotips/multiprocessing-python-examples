####################################
# Multiprocessing baseline example #
# https://vicsprotips.com          # 
# Vic Baker                        #
####################################

import multiprocessing

def doWork(params):
    """
    Each item from the queue will be processed here

    """
    try:
        data = params
        print(f"doWork is processing: {data}")
        return data
    except Exception as e:
        return f"Error processing {data}: {e}"

if __name__ == '__main__':

    # define a queue with a range of numbers
    queue = list(range(1, 11))
    print(queue)
    print("Queue created.  Starting pool")
    
    pool = multiprocessing.Pool()
    results = pool.map(doWork, queue)
    pool.close()

    print("Pool done!  Printing results:")
    for r in results:
        print(r)
    