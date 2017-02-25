#εργασία 3 (εργασία χωρισμένη σε δύο μέρη)
#έκδοση python 3.6

print ("Γ---------------------------------------")
print ("|Εισαγωγή στην επιστήμη των υπολογιστών")
print ("|Εργασία 3")
print ("L---------------------------------------")

lstListOfNumbers = list() #δημιουργία λίστας (lst)

nTotalNumbers = int(input("Πόσους αριθμούς θα καταχωρήσετε στη λίστα: "))
#έλεγχος για την τιμή της τιμής
while nTotalNumbers < 0:
    nTotalNumbers = int(input("Μη αποδεκτός αριθμός. Πληκτρολογήστε έναν αριθμό μεγαλύτερο ή ίσο του μηδενός: "))

if nTotalNumbers > 0:
    print ("Επιλέξτε τους αριθμούς σας")
    for nCounter in range(int(nTotalNumbers)):
        number = int(input("τιμή αριθμού: "))
        lstListOfNumbers.append(int(number))
    print ("Η λίστα σας: ", lstListOfNumbers)

    #έλεγχος των items στη λίστα
    # - ανίχνευση μηδενικών
    # - διαγραφή τους από την εκάστωτε θέση τους
    # - δημιουργία "μετακίνηση" μηδενικού στο τέλος της λ΄ίστας
    nZerosCounter = 0 #μετρητής μηδενικών
    nListPointer = 0
    while 1: #σταθερή συνθήκη, πάντα True, μεχρι να μπει στο break
        if lstListOfNumbers[nListPointer] == 0:
            del lstListOfNumbers[nListPointer] #διαγραφή μηδενικού
            lstListOfNumbers.append(0) #δημιουργία "μετακίνηση" μηδενικού στο τέλος της λίστας
            nZerosCounter += 1 #έτοιμα (στο τέλος) μηδενικά
        if lstListOfNumbers[nListPointer] != 0:
            nListPointer += 1 #μετακίνηση του pointer στο επόμενο item
        if (nTotalNumbers - nZerosCounter) == nListPointer or nListPointer == nTotalNumbers:
            break #σταματαει το loop όταν όλα τα μηδενικά φτάσουν στο τέλος της λίστας ή δεν υπάρχουν μηδενικά στη λίστα γενικά
    print ("Τέλος προγράμματος. Η νέα λίστα σας είναι: ", lstListOfNumbers)
else:
    print ("Δεν υπάρχουν στοιχεία στον πίνακα, ξανατρέξτε το πρόγραμμα")
