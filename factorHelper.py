#my ineficient take on the quadform script found on my friend joaquin's calculator
# this script uses the guess and check method of finding the factors of numbers
# in retrospect the quadratic equation would have been but in retrospect sucks!

def factors(x):
    '''
    input x = what number you would like the factors of
    outputs a factor, what that confirmed factor divided by x equals
    '''
    factorList = []
    for i in range(1,abs(x)+1):       #BEWWARE there was a '+1' after abs(x) incase that was some kind of redunency protection
        if abs(x) % i == 0:
            factorList.append(i)
            factorList.append(int(x/i))    #removed |(int(abs(x)/i)) |
    return factorList

print('aX^2 + bx + c')
print('what is a?')
a = int(input())
print('what is c?')
c = int(input())
print('what is b?')
addedFactor = int(input())
multFactor = a * c

prime = True   #for later to show if unfactorable
#print(factors(multFactor))

baseFactors = factors(multFactor)
allNegFactors = baseFactors[:]
halfNegFactors = baseFactors[:]

for i in range(len(baseFactors)):
    allNegFactors[i] = allNegFactors[i] * (-1)

for i in range(0,len(baseFactors),2):
    halfNegFactors[i] = halfNegFactors[i] * (-1)

#allFactors = [baseFactors] + [allNegFactors] + [halfNegFactors]
#^ i dont know how to deal with nested lists

allFactors = baseFactors[:]
for i in range(len(baseFactors)):
    allFactors.append(allNegFactors[i])
for i in range(len(baseFactors)):
    allFactors.append(halfNegFactors[i])

#print(allFactors)

for i in range(0,len(allFactors),2):
    if allFactors[i] + allFactors[i+1] == addedFactor:
        prime = False
        print(allFactors[i] , '+', allFactors[i+1],' = ', addedFactor)
        print(allFactors[i] , '*', allFactors[i+1],' = ', multFactor)
        #factor1 = allFactors[i]
        #factor2 = allFactors[i+1]
        trueFactorList = [allFactors[i],allFactors[i+1]]
        print(trueFactorList)
        break

if prime == True:
    print('the equation is prime')

def GCF(factor,c):
    '''
    factor and c 's common factor will be searched recursively
    if a common factor is not found it will print whatever two reduced numbers
    it has in the form of a tuple
    input = (factor,c)
    output = (factor,c)
    '''
    lesserRange = 0
    if abs(factor) >= abs(c):
        lesserRange = abs(c)
    else:
        lesserRange = abs(factor)   #i dont even use the lesser range and i think i should
    for i in range(2,abs(c)):       #range starts @ 2 cause x%1 == 0 would be too(too(too(too...))) recursive
        if factor % i == 0 and c % i == 0:
            factor = int(factor/i)
            c = int(c/i)
            GCF(factor,c)
    return (factor,c)

def factorFormer(factor,c):
    '''
    from the inputs it will (kinda)convolutedly try to print a string like this
    (x+1)
    what is expected:
        number before x must be positive
        numbers must be reduced as far as posible
        c has to display if it is positive or negative as a string (i dont know how to do it another way)
    input = (factor,c)
    output = '(x+1)'
            fun fact 'tuple does not support item assignment'
    '''
    if int(factor * -1) == abs(factor):
        factor = factor * -1
        c = c * -1
    reducedFactor = GCF(factor,c)

    factor = reducedFactor[0]
    c = reducedFactor[1]

    if c * -1 != abs(c):
        c = '+'+ str(abs(c))

    output = ['(',str(factor),'x',str(c),')']
    output = ''.join(output)
    return output

for i in range(2):
    print(factorFormer(trueFactorList[i],c))


'''
print(baseFactors)
print(allNegFactors)
print(halfNegFactors)
print('----')
print(allFactors)
'''


#print(allFactors)
#factors(multFactor)


#DONE make factors export a list with corresponding factors(for redunency protection)
#DONE allow for added input to be compared to every set of corresponding factors
#DONE(including negative variations) to see what combination works with the factorization
#note total number of factors = (len(factorList)/2) (sub 4 or 2 depeneding on how you feel towards 1 * num)
#DONE make a jumbled mess of a prinint format for ax^2 + bx + c with GCF() function
#TODO maybe once this is all over, take a leap into python gui or a module like that to
#^TODO tldr do front end stuff
#^^TODO nah screw front end
#TODO make some failsafe for this situation
#           ax^2 + bx -c
# the negative C messes up everything so i think its prime
#       IT CAN BE BUT IT IS NOT IMPOSIBLE
#note on line 14 (or if i add stuff (i had to take out factorList.append(int(x/i))  )
#   in case stuff doesnt work later, change the true factor conditon for both x + x+1 = b AND x * x+1 = a*c

#	TODO PROBLEM there is an instance where a factor will not properly reduce. this is probably an error with the
# 		GCF() function[greates common factor] . i need to better integrate the lesser range snipit in the code
# 			first i want to find an example of it . maybe (x-31)(x+17)

#lesser TODO rework the GCF() to work with reducing the entire quadratic (or is it trinomial)
