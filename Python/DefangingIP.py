def defangIPaddr(address):
    addrlist = list(address.split('.'))
    newaddr = '[.]'.join(addrlist)
    return newaddr


address = "10.6.136.182"
newaddr = defangIPaddr(address)
print(newaddr)
