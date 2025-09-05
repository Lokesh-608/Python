#Strings Collection of characters
a = 'Lokesh'
b = "Lokesh"
c = '''Lokesh'''
print(type(a),type(b),type(c))
#lower
p="Python Life"
print(p.lower())
#upper
p="python life"
print(p.upper())
#endswith()
p = "Python life"
print(p.endswith("e"))
print(p.startswith("P"))
#replace
p = "python life"
print(p.replace("life","program"))
#find ,index is used to find the index number
p = "python life"
print(p.index("p"))
print(p.find("t"))
#count
p = "python life"
print(p.count("t"))
#remove
p = "python life"
print(p.removeprefix("python"))
print(p.removesuffix("life"))
#split
p = "python life"
print(p.split())
#strip
p = "  python life  "
print(len(p)) 
x = p.strip()
print(len(x))
a= p.lstrip()
b= p.rstrip()
print(a)
print(b)
print(len(a))