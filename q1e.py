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
    letter = (textArr[i] + keyArr[i % 5]) % 26
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