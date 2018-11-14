from ipaddress import ip_network, ip_address
import socket

# A script to determine whether certain domains run through an organization.

DOA_Cidr1 = ip_network('CIDR RANGE')
DOA_Cidr2 = ip_network('CIDR RANGE')
DOA_Cidr3 = ip_network('CIDR RANGE')
DOA_Cidr4 = ip_network('CIDR RANGE')
DOA_Cidr5 = ip_network('CIDR RANGE')
DOA_Cidr6 = ip_network('CIDR RANGE')

#file path and open

with open("ip.txt", "r") as y:
    for host in y:
        if host.strip():
            try:
                domain = socket.gethostbyname(host.strip())
                DOAip = ip_address(domain)
                if DOAip in DOA_Cidr1 or DOAip in DOA_Cidr2 or DOAip in DOA_Cidr3 or DOAip in DOA_Cidr4 or DOAip in DOA_Cidr5\
                        or DOAip in DOA_Cidr6:

                    print(host + ' > ' + domain + ' runs through <Insert Organization>')
                else:
                    print(host + ' >  does not run through <Insert Organization>')
            except:
                print(host + ' > is Not resolved')




