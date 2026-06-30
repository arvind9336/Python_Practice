# What is dictionary ?
# Dictionary are used to store data in key : value pairs.
# Dictionary is a collection which is order, changeable, and do not allow duplicate

d={
    "name":"Arvind",
    "age":24,
    "city":"Varanasi"
}
print(d)
d["city"]="Delhi"
print(d)


# Update:
d.update({"city":"Ghaziabad"})
print(d)