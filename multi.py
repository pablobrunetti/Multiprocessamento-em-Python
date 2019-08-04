import time
import multiprocessing 
import datetime

def basic_func(x):
    if x == 0:
        return 'zero'
    #elif x%2 == 0:
    #    return 'even'
    else:
        return 'odd'

def multiprocessing_func(x):
    arq = open('processo'+str(x)+'.txt', 'w+')
    i=x
    print('Processo:' + str(x))
    while True:
        #time.sleep(2)
        timestamp = datetime.datetime.utcnow().isoformat()
        arq.write(str(i)+': '+str(timestamp)+'\n')
        #print('{} squared results in a/an {} number'.format(i, basic_func(y)))
        i=i+1
        if(i == 10) and x == 0:
            break
        if(i == 30) and x == 1:
            break
    print('Fim do Processo:'+str(x))

    arq.close()

def manager_func():
    i = 0
    processes = {}
    vetorProcesses = []
    while True:
        for i in range(0,2):
            if(i in processes):
                a = 0
            else:
                p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
                processes[i] = p
                p.start()
                vetorProcesses.append(processes[i])   
        for process in vetorProcesses:
            process.join()
    
if __name__ == '__main__':
    starttime = time.time()
    processes = []
    
    #for i in range(0,2):
    p = multiprocessing.Process(target=manager_func)
    #processes.append(p)
    p.start()
        
    #for process in processes:
    #    process.join()
        
    print(' {} seconds'.format(time.time() - starttime))