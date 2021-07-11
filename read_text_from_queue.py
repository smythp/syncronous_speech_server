import rpyc

c = rpyc.connect("localhost", 18861)

c._config['sync_request_timeout'] = None

while True:
    c.root.pop_and_read()




