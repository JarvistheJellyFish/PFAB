gpas = {"Lassoff":3.12,
 "Johnson":2.22,
 "Reich":3.59,
 "Honeychurch":2.98,
 "Maini":3.11,
 "Levin":2.88,
 "Marcus":2.77,
 "Banks":3.71}

average = 0
for i in gpas:
    print "Last Name:",i,"\tGPA:",gpas[i]
    average+=gpas[i]

print ""

average/=len(gpas)
print "Average GPA:",average

a = sorted(gpas.values())
a.reverse()

print ""

x=0
for j in a:
    x+=1
    for i in gpas:
        if gpas[i]==j:
            print "Rank %d: %s"%(x,i)
            continue
