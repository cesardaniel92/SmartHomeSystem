


testThread = threading.Thread(target=thread_function, args=(1,))

def thread_function(name):
    print "thread doing work ..."
    time.sleep(5)
