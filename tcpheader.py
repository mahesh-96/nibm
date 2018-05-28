

from c type import*
import structure
class ip(structure)

def _ _init_ _(self,socket_buffer=none);
    self.src_address = socket.inet - nto a(struct.pack("@i",selfsrc))


def _ _new_ _(self,socket-buffer=none);
    return self.from _buffer_copy(socket-buffer)

    - fiels_ = [
                ("srcport",c-u int 32),
                ("dstport",c-u int 32),
                ("sequence num",c-u int 64),
                ("acknum",c-u int 64),
                ("offset",c-ubyte,4),
                ("reserved",c-byte,4),
                ("tcpflag",c-byte,8),
                ("window",c-u int 32),
                ("cheacksum",c-u int 32),
                ("urgennt pointer",c-u int 32),
                (
    close fiels            
