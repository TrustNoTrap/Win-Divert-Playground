#########################################################################################################
# Try to surf the web on port 8080 when trying out this script                                          #
#########################################################################################################

import pydivert
from datetime import datetime

print('Starting pydivert...\n\n')
dst_port = 8080
src_port = 443
handle = []
try:
    with pydivert.WinDivert(f'tcp.DstPort == {dst_port} or tcp.SrcPort == {src_port}') as w:
        for packet in w:
            # print(packet)
            if packet.dst_port == dst_port:
                if packet.dst_addr not in handle:
                    handle.append(packet.dst_addr)
                print(datetime.now(), f'Packet DST port: {packet.dst_port}\tRewriting to {src_port}') #\nFull packet:', packet)
                packet.dst_port = src_port
            elif packet.src_port == src_port and packet.src_addr in handle:
                print(datetime.now(), f'Packet SRC port: {packet.src_port}\tRewriting to {dst_port}') #\nFull packet:', packet)
                packet.src_port = dst_port
            w.send(packet)
except Exception as e:
    print('Got error: ', e)

print('Done\n\n')
