#εργασία 4
#έκδοση python 3.6

print ("Γ---------------------------------------")
print ("|Εισαγωγή στην επιστήμη των υπολογιστών")
print ("|Εργασία 4")
print ("L---------------------------------------")

lstListOfNumbers = list() #δημιουργία λίστας (lst)

nTotalNumbers = int(input("Πόσους αριθμούς θα καταχωρήσετε στη λίστα: "))
while nTotalNumbers <= 5: #έλεγχος για την τιμή
    #για να υπάρχει τυπική απόκλιση χωρίς τις δύο μεγαλύτερες και μικρότερες τιμές, η λ΄ίστα απαιτε΄΄ι τουλάχιστον 6 τιμές
    nTotalNumbers = int(input("Μη αποδεκτός αριθμός. Πληκτρολογήστε έναν αριθμό μεγαλύτερο ή ίσο του έξι: "))

#διάβασμα αριθμών από τον χρήστη
print ("Επιλέξτε τους αριθμούς σας")
for nCounter in range(int(nTotalNumbers)):
    number = float(input("τιμή αριθμού: "))
    lstListOfNumbers.append(number)
#end of "for"
lstListOfNumbers.sort() #αυτόματη ταξινόμηση

nSum1 = 0 #αθροισμα για υπολογισμο μέσου όρου
counter1 = 2 #δείκτης λίστας
while counter1 <= (nTotalNumbers - 3):
    nSum1 = nSum1 + lstListOfNumbers[counter1]
    counter1 += 1

nAverageValue = nSum1 / (len(lstListOfNumbers)-4) #μέσος όρος των τιμών που χρησιμοποιούνται για τον υπολογισμό του μ.ό.
counter2 = 2 #δείκτης λίστας
nSum2 = 0 #μέρος του τύπου της τυπικής απόκλισης (άθροισμα)
while counter2 <= (nTotalNumbers - 3):
    nSum2 = nSum2 + (lstListOfNumbers[counter2] - nAverageValue)**2
    counter2 += 1
#end of "while"
nYporrizo = nSum2 / (len(lstListOfNumbers)-4) #μέρος του τύπου της τυπικής απόκλισης (υπόρριζο)
nTypikiApoklisi = (nYporrizo)**(1/2) #τιμή τυπικής απόκλισης
#γενικά --> τυπικη απόκλιση = (1/(len(lstListOfNumbers)-4)*nSum2)**(1/2)
print ("Τέλος προγράμματος. Η τυπική απόκλιση των αριθμών σας είναι: ", nTypikiApoklisi)
