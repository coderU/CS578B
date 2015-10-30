DEBUG = True

def reverse(B):
    if B == 'T':
        return 'F'
    else:
        return 'T'
def init_condition(condition):
    condition['B=T'] = 0.001
    condition['E=T'] = 0.002
    condition['B=F'] = 0.999
    condition['E=F'] = 0.998

    condition['A=T|B=T,E=T'] = 0.95
    condition['A=F|B=T,E=T'] = 0.05

    condition['A=T|B=T,E=F'] = 0.94
    condition['A=F|B=T,E=F'] = 0.06

    condition['A=T|B=F,E=T'] = 0.29
    condition['A=F|B=F,E=T'] = 0.71

    condition['A=T|B=F,E=F'] = 0.001
    condition['A=F|B=F,E=F'] = 0.999

    condition['J=T|A=T'] = 0.9
    condition['J=T|A=F'] = 0.05

    condition['M=T|A=T'] = 0.7
    condition['M=F|A=T'] = 0.3

    condition['M=T|A=F'] = 0.01
    condition['M=F|A=F'] = 0.99

def bruteforce(condition, check, B, E, A, M):
    hash = 'B='+B+',E='+E+',A='+A+',M='+M+',J=T'
    value = check.get(hash)
    if value != None:
        return
    else:
        val = 0
        first = 'B='+B
        second = 'E='+E
        third = 'A='+A+'|B='+B+',E='+E
        fourth = 'M='+M+'|A='+A
        fifth = 'J=T|A='+A

        val = condition[first]*condition[second]*condition[third]*condition[fourth]*condition[fifth]
        check[hash] = val
        if DEBUG:
            print "------------DEBUG---------------"
            print hash+":"+str(val)
        bruteforce(condition, check,reverse(B),E,A,M)
        bruteforce(condition, check,B,reverse(E),A,M)
        bruteforce(condition, check,B,E,reverse(A),M)
        bruteforce(condition, check,B,E,A,reverse(M))


check = {}
condition = {}
init_condition(condition)
if(DEBUG):
    print "------------DEBUG---------------"
    print condition
bruteforce(condition, check, 'T','T','T','T');
sum = 0
for key in check:
    sum+=check[key]

print "------------Problem 1.1:Brute Force---------------"
for key in check:
    print key+":"+str(100*check[key]/sum)+"%"
