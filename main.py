import socket
import struct
import random


def build_dns_query(hostname):
    # Generating a random 16-bit ID
    dns_id = random.randint(0, 65535)

    # building a header. packs the DNS ID in network byte order ('!H' means a 16-bit unsigned integer in network byte order).
    header = struct.pack('!H', dns_id)
    # packs the flags. In this case, we set the "recursion desired" bit to 1, indicating that we want the DNS server to perform recursive resolution for us.
    header += struct.pack('!H', 0x0100)

    # For this initial query your message should have empty answer, authority and additional sections.
    # Number of questions, answer resource records, authority resource records, and additional resource records (16 bits each)

    header += struct.pack('!HHHH', 1, 0, 0, 0)

    # DNS question

    question = b''
    for label in hostname.split('.'):
        question += struct.pack('B', len(label))
        question += label.encode()

    question += b'\x00'  # End of the domain name
    question += struct.pack('!H', 1)  # Query type (A record)
    question += struct.pack('!H', 1)  # Query class (IN)
    return header + question


dns_query = build_dns_query('www.google.com')


print(dns_query.hex())


