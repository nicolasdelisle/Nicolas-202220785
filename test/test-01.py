import ipaddress

def subnet_calculator():
    print("== Subnet Calculator ==")
    
    # Ask for input
    ip_input = input("Enter an IP address (e.g., 192.168.1.0/24): ")
    
    try:
        network = ipaddress.IPv4Network(ip_input, strict=False)

        print(f"\nNetwork Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Number of Usable Hosts: {network.num_addresses - 2}")
        print(f"First Host: {list(network.hosts())[0]}")
        print(f"Last Host: {list(network.hosts())[-1]}")
        
    except ValueError :
        print("Invalid input. Please use correct format (e.g., 192.168.1.0/24)")

# Main
subnet_calculator()