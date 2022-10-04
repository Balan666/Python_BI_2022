#dictionaries for different nucleic acids
DNAtoRNA = {'A':'U', 'T':'A', 'G':'C', 'C':'G', 'a':'u', 't':'a', 'c':'g', 'g':'c'}
RNAtoDNA = {'A':'T', 'U':'A', 'G':'C', 'C':'G', 'a':'t', 'u':'a', 'c':'g', 'g':'c'}
DNAtoDNA = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'a':'t', 't':'a', 'c':'g', 'g':'c'}
RNAtoRNA = {'A':'U', 'U':'A', 'G':'C', 'C':'G', 'a':'u', 'u':'a', 'c':'g', 'g':'c'}


def DNAorRNA(seq):          #to define is 'seq' a DNA or an RNA sequence
    if (seq.find('U') != -1) or (seq.find('u') != -1):      #there is Uracil
        return('RNA') 
    else:      
        return('DNA')        

def check_validity(seq):    #check if its a nucleic acid
    if (seq.find('U') != -1)&(seq.find('T') != -1) or\
                (seq.find('U') != -1)&(seq.find('t') != -1) or\
                (seq.find('u') != -1)&(seq.find('T') != -1) or\
                (seq.find('u') != -1)&(seq.find('t') != -1):
        print('Nucleic acid can`t contain both U and T, try again')
        return(False)
    for i in seq:
        if (i not in DNAtoRNA.keys()) & (i not in RNAtoDNA.keys()):
            print('weird symbols... can`t transcribe')
            return(False)
    return(True)

'''
>>> s = input('Enter command:')
Enter command:reverse transcribe
>>> print(s)
reverse transcribe
>>> if s == 'reverse transcribe':
...     reverse_transcribe()
'''

while True:    #endless cycle in which program works
    command = str(input('Enter command:'))  #user gives a command
    if command == 'exit':                    #exit
        print('Goodbye!')
        break
    elif command == 'transcribe':            #transcribe DNA to RNA, its impossible to transcribe RNA to DNA
        seq = str(input('enter sequence:'))  #user gives a sequense
        if not check_validity(seq):     #check if sequence is valid (right)   
            continue                         #start the cycle from the beginning
        if DNAorRNA(seq) == 'DNA':           #check if its DNA or RNA
            print(''.join(DNAtoRNA[x] for x in seq))
        else:
            print('Only DNA can be transcribed')
    elif command == 'reverse':              # reverse a sequense
        seq = str(input('enter sequence:'))  #user gives a sequense
        if not check_validity(seq):     #check if sequence is valid (right)
            continue
        print(seq[::-1])
    elif command == 'complement':
        seq = str(input('enter sequence:'))  #user gives a sequense
        if check_validity(seq) == False:     #check if sequence is valid (right)
            continue
        if DNAorRNA(seq) == 'DNA':           #check if its DNA or RNA
            print(''.join(DNAtoDNA[x] for x in seq))
        else:
            print(''.join(RNAtoRNA[x] for x in seq))
    elif command == 'reverse complement':
        seq = str(input('enter sequence:'))  #user gives a sequense
        if check_validity(seq) == False:     #check if sequence is valid (right)
            continue
        if DNAorRNA(seq) == 'DNA':           #check if its DNA or RNA
            print(''.join(DNAtoDNA[x] for x in seq[::-1]))
        else:
            print(''.join(RNAtoRNA[x] for x in seq[::-1]))

