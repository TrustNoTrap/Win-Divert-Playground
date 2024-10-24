#########################################################################################################
# Use this script with the Python http server module to experience a simple network stack interception #
#########################################################################################################

import pydivert
from datetime import datetime

try:
    with pydivert.WinDivert('tcp.DstPort == 80 or tcp.SrcPort == 8000') as w:
        for packet in w:
            print(packet)
            if packet.dst_port == 80:
                print(datetime.now(), 'Packet dest port: ', packet.dst_port, '\nRewriting to 8000') #\nFull packet:', packet)
                packet.dst_port = 8000
            elif packet.src_port == 8000:
                print(datetime.now(), 'Packet src port: ', packet.src_port, '\nRewriting to 80') #\nFull packet:', packet)
                packet.src_port = 80
            w.send(packet)
except Exception as e:
    print('Got error: ', e)
