
#Question 1

#(a) What is the population variance of the relative letter frequencies in English text?
#    Population variance = 0.0010405667735207099
def popVar(N, xi, mu):
    return (1.0/N) * ()

frequency = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228, "G": .02015, "H": .06094, "I": .06996, "J": .00153, "K": .00772, "L": .04025, "M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987, "S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150, "Y": .01974, "Z": .00074 }
plaintext = 'ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt' \
            'ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev' \
            'enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacya' \
            'ndpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandab' \
            'useactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindou' \
            'btwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper'

N = 26
mu = 0.0
sum = 0.0

for entries in frequency:
    mu = mu + frequency[entries]
mu = mu/N

for entries in frequency:
    diff = frequency[entries] - mu
    diff = diff * diff
    sum = sum + diff
sum = sum/N

print(sum)


#(b) What is the variance of the relative letter frequencies in the given plaintext?
#    variance = 0.03946851225697378

def popVarB(N, xi, mu):
    return (1.0/N) * ()

frequency = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
plaintext = 'ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt' \
            'ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev' \
            'enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacya' \
            'ndpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandab' \
            'useactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindou' \
            'btwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper'

N = 26.0
mu = 0.0
sum = 0.0
newString = plaintext.upper()

for letters in newString:
    if (frequency [letters] == 0):
        frequency[letters] = frequency[letters] + newString.count(letters)

for letters in frequency:
    frequency[letters] = frequency[letters] / newString.__len__()
    sum = sum + frequency[letters]

for entries in frequency:
    mu = mu + frequency[entries]
mu = mu/N

for entries in frequency:
    diff = frequency[entries] - mu
    diff = diff * diff
    sum = sum + diff
sum = sum/N

print(sum)


#(c) Encrypt plaintext with a Vigenere cipher and the given key:yz, xyz, wxyz, vwxyz, uvwxyz
key = 'uvwxyz'
keyOriginal = 'uvwxyz'
ciphertext = ''

plaintext = 'ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt' \
            'ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev' \
            'enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacya' \
            'ndpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandab' \
            'useactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindou' \
            'btwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper'

plainLength = plaintext.__len__()
keyLength = key.__len__()
newLength = plaintext.__len__() / key.__len__()
newtext = plaintext.lower()
keyArr = []
textArr = []

for i in key:
    keyArr.append(ord(i))

for i in plaintext:
    textArr.append(ord(i))

for i in range(plainLength):
    letter = (textArr[i] + keyArr[i % keyLength]) % 26
    ciphertext = ciphertext + chr(letter + 65)

print(ciphertext)


frequency = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
N = 26.0
mu = 0.0
sum = 0.0

for letters in ciphertext:
    if (frequency [letters] == 0):
        frequency[letters] = frequency[letters] + ciphertext.count(letters)

for letters in frequency:
    frequency[letters] = frequency[letters] / ciphertext.__len__()
    sum = sum + frequency[letters]

for entries in frequency:
    mu = mu + frequency[entries]
mu = mu/N

for entries in frequency:
    diff = frequency[entries] - mu
    diff = diff * diff
    sum = sum + diff
sum = sum/N

print(sum)


'''
for i in range(int(newLength)):
    key = key + keyOriginal

for i in range(plainLength):
    x = (ord(plaintext[i]) + ord(key[i])) % 26
    print(chr(x))
    ciphertext = ciphertext + (chr(x))
    print(type(ciphertext))

print(ciphertext)'''




#(d)
#Question 1
#(c) Encrypt plaintext with a Vigenere cipher and the given key:yz, xyz, wxyz, vwxyz, uvwxyz
key = 'uvwxyz'
keyOriginal = 'uvwxyz'
ciphertext = ''

plaintext = 'ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedt' \
            'ocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesev' \
            'enprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyineecsisthatyoumustrespecttheprivacya' \
            'ndpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandab' \
            'useactcfaaafederalstatutethatbroadlycriminalizescomputerintrusionthisisoneofseverallawsthatgovernhackingunderstandwhatthelawprohibitsifindou' \
            'btwecanreferyoutoanattorneypleasereviewitsspoliciesonresponsibleuseoftechnologyresourcesandcaenspolicydocumentsforguidelinesconcerningproper'

plainLength = plaintext.__len__()
keyLength = key.__len__()
newLength = plaintext.__len__() / key.__len__()
newtext = plaintext.lower()
keyArr = []
textArr = []

for i in key:
    keyArr.append(ord(i))

for i in plaintext:
    textArr.append(ord(i))

for i in range(plainLength):
    letter = (textArr[i] + keyArr[i % keyLength]) % 26
    ciphertext = ciphertext + chr(letter + 65)


print(ciphertext)

even = ''
odd = ''

EBool = True

for letters in ciphertext:
    if (EBool):
        even = even + letters
        EBool = False
    else:
        odd = odd + letters
        EBool = True

print(even)
print(odd)





frequency = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
N = 26.0
mu = 0.0
sum = 0.0

for letters in even:
    if (frequency [letters] == 0):
        frequency[letters] = frequency[letters] + even.count(letters)

for letters in frequency:
    frequency[letters] = frequency[letters] / even.__len__()
    sum = sum + frequency[letters]

for entries in frequency:
    mu = mu + frequency[entries]
mu = mu/N

for entries in frequency:
    diff = frequency[entries] - mu
    diff = diff * diff
    sum = sum + diff
sum = sum/N
evenSum = sum



sum = 0.0
mu = 0.0
frequency = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

for letters in odd:
    if (frequency [letters] == 0):
        frequency[letters] = frequency[letters] + odd.count(letters)

for letters in frequency:
    frequency[letters] = frequency[letters] / odd.__len__()
    sum = sum + frequency[letters]

for entries in frequency:
    mu = mu + frequency[entries]
mu = mu/N

for entries in frequency:
    diff = frequency[entries] - mu
    diff = diff * diff
    sum = sum + diff
sum = sum/N

oddSum = sum
print(oddSum)
print(evenSum)
print((oddSum + evenSum) / 2)

#(e) uses (d) but only changes the key length, not the key itself


#Question 2


#Question 3 What is "snakeoil cryptography?" How does it relate to the exercise above?
#Snakeoil cryptography is a cryptographic product that claims to work but doesn't hence the name snake oil.
#It is difficult for the user to tell if the product is secure or not and this relates to the exercise above
#because even though the vinegere cipher is some level of security, it is not fully secure and should
#not be used for the public as the key can be found