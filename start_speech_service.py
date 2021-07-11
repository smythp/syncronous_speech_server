from speak import speak
import rpyc
import queue


class MyService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass


    def exposed_remote_speak(self, text_to_speak):
        self.speech_queue.put(text_to_speak, block=True, timeout=None)

    def exposed_get_queue_length(self):
        return self.speech_queue.qsize()


    speech_queue = queue.Queue(maxsize=10000)


    def exposed_pop_and_read(self):
        text = self.speech_queue.get()
        speak(text)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()
    
