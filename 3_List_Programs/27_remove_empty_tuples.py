# program to remove empty tuples from a list

tuples = [(), ('ram','15', '8'), (), ('laxman', 'urmila'), ('krishna', 'rukmani'),
          ('', ''), ()]

#tuples = filter(None, tuples)
tuples = [t for t in tuples if t]

print(str(tuples))
