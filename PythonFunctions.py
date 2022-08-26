import re

#Definieren der Funktionen

def create_phone_number(n):
    string = ''.join(str(x) for x in n)
    return '({0}) {1}-{2}'.format(string[:3],string[3:6],string[6:])

def duplicate_count(text):
    result = 0
    uniqueChars = str(set(text.lower()))
    for i in range(len(uniqueChars)):
        count = 0
        for j in range(len(text)):
            if(uniqueChars[i] == text[j].lower()):
                count += 1
        if(count > 1):
            result += 1
    return result

def count_smileys(arr):
    count = len((re.findall(":-?~?D|:-?~?\)|;-?~?D|;-?~?\)",str(arr))))
    return count

def find_it(seq):
    numbers = set(seq)
    for n in numbers:
        if(seq.count(n) % 2 == 1):
            return n


#Aufruf der Funktionen

#Eine Telefonnummer aus einem String erzeugen
print("Eine Telefonnummer aus einem String erzeugen")
print("Eingabe: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 | Loesung: " + create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print("Eingabe: 0, 2, 3, 0, 5, 6, 0, 8, 9, 0 | Loesung: " + create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))
print()

#In einem String die mehrfach vorkommenden Buchstaben zählen
print("In einem String die mehrfach vorkommenden Buchstaben zaehlen")
print("Eingabe: abcdeaB | Loesung: " + str(duplicate_count("abcdeaB")))
print("Eingabe: Indivisibilities | Loesung: " + str(duplicate_count("Indivisibilities")))
print()

#Alle vorkommenden Smileys zählen | :) :D ;-D :~)
print("Alle vorkommenden Smileys zaehlen | :) :D ;-D :~)")
print("Eingabe: :D,:~),;~D,:) | Loesung: " + str(count_smileys([':D',':~)',';~D',':)']))) 
print("Eingabe: ;], :[, ;*, :$, ;-D | Loesung: " + str(count_smileys([';]', ':[', ';*', ':$', ';-D'])))
print()

#Die ungrade vorkommende Zahl ausgeben
print("Die ungrade vorkommende Zahl ausgeben")
print("Eingabe: 20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5 | Loesung: " + str(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])))
print("Eingabe: 5,4,3,2,1,5,4,3,2,10,10 | Loesung: " + str(find_it([5,4,3,2,1,5,4,3,2,10,10])))
print()
