# python_script
factorial.py 使用mulitprocessing模块,使用map,reduce  
http_server_example.py 用fork模式编程  
http_server_threads.py 多线程模式  
http_server_threads_2.py 改写http_server_threads.py,不用线程池，用accept接受之后开线程的方式去处理连接  
mulitProcess.py 使用mulitprocessing模块，使用多进程处理问题  
readWord.py 滚动读取1024个字符统计出现的单词  
th_num.py 使用threading，多线程计算，体现python全局锁的问题  
thread_example.py 如何使用threading模块  
thread_example_2.py 不继承Thread类启动新的线程  
thread_pool.py python3的线程池例子 
thread_queue_event_example.py 实例化一个event对象，可以让生产者监视消费者进程  
thread_queue_example.py 线程间的通讯用queue队列实现，队列自身实现锁的功能  
thread_queue_example_2.py 生产者将一个结束信号放入队列，消费者监听到这个信号之后将信号重新放入队列，结束自己  
thread_queue_example_3.py生产者将数据放入queue，两个消费者来取判断数据类型符合条件的处理，不符合条件重新放回queue  
thread_queue_ring.py 类似thread_queue_example_3.py 生命十个线程处理数据形成一个环  
