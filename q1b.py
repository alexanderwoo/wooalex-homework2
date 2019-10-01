
#Question 1

#(b) What is the variance of the relative letter frequencies in the given plaintext?
#    variance = 0.03946851225697378

def popVar(N, xi, mu):
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