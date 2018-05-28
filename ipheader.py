import structure
class ip(struct)

def _ _init_ _(self,socket_buffer=none);
    self.src_address = socket.inet - nto a(struct.pack("@i",selfsrc))


def _ _new_ _(self,socket-buffer=none);
    return self.from _buffer_copy(socket-buffer)

    - fiels_ = [
                ("version",c-byte,4),
                ("ihl",c-byte,4),
                ("tos",c-ubyte),
                ("len",c-ubyte),
                ("srcmac",c-byte,8),
                ("dstmac",c-byte,8),
                ("ipflag",c-byte,3),
                ("fregmntoff",c-u int 14),
                ("ttl",c-ubyte),
                ("protocol",c-ubyte),
                ("checsum",c-u int 32),
                ("src",c-u int 32),
                ("dessrc",c-u int 32)
]
    close fiels            
