payload = 100
udp_wire = 20 + 8 + payload
tcp_wire = 20 + 20 + payload
print(f"UDP wire = {udp_wire} B, overhead = {(udp_wire-payload)/udp_wire*100:.1f}%")
print(f"TCP wire = {tcp_wire} B, overhead = {(tcp_wire-payload)/tcp_wire*100:.1f}%")