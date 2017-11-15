s = 'I love to write python'

# print each value of s
for i in s:
    print i

# print 5th and last
print s[4]
print s[-1]

# print length of s
print len(s)

# print 1st letter by index
print s[0]
print s[0][0]
print s[0][0][0]


############

# split strings and look for a letter in it.
s_splits = s.split()
print s_splits

for i in s_splits:
    if i.find('i') > -1:
        print "I found 'i' in: '{0}'".format(i)


#####

something = 'Completely different'

print dir(something) #find possible functions within 'something'

print something.count('t') # count how many times 't'
print something.find('plete') #find which index position is 'plete'
print something.split('e') # split 'something' by 'e'

# replace different with silly 
thing2 = something.replace('different','silly')
print thing2

# the below does not work because strings cannot be changed

#something[0] = 'B'
#print something

######
