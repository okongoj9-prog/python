# python tuple - is a type of a list that is not mutanble (unchangeble)
# To introduced a tuple we use the brackets()


counties = ("Nairobi", "Machakos", "Kisumu", "Kisii", "Narok", "Mombasa", "Lamu", "Kilifi")
print(counties)
print(type(counties))

# A tuple stores is items on indexes . Also strart from index zero.
print(counties[3])

# slicing of tuple
print(counties[3:])

# Print from machakos to mombasa
print(counties[1:6])

# Note below code will show an error. Why bcz a tuple is imutable...
counties.append("Nakuru")
print(counties)