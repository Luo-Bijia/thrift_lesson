from match_client.match import Match
from match_client.match.ttypes import User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from sys import stdin

def operate(op, user_id, username, score):
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol)

    # Connect!
    transport.open()
    user = User(user_id, username, score)
    if op == 'add':
        client.add_user(user, "")
    elif op == 'remove':
        client.remove_user(user, "")

    # Close!
    transport.close()

def main():
    for line in stdin:			# 每次循环读取一行（直到遇到\n后阻塞等待下一次输入），直到遇到EOF（文件结束，Ctrl+D）才会结束
        op, user_id, username, score = line.split(' ')
        operate(op, int(user_id), username, int(score))     # 每次读取到新参数时都将进行一次Socket连接

if __name__ == "__main__":
    main()
