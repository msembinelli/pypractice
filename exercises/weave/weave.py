from queue import Queue

def weave(q1, q2):
    q_out = Queue()
    while q1.peek() is not None or q2.peek() is not None:
        if q1.peek() is not None:
            q_out.add(q1.remove())
        if q2.peek() is not None:
            q_out.add(q2.remove())
    return q_out