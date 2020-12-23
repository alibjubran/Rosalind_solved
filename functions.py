#For counting the nucleotides of at strand
def countnucleotides (strand):
    nucleotides=list(set(strand))
    nucleotides.sort()
    counts=[]
    for i in nucleotides:
        counts.append(strand.count(i))
    counted_nucleotides=list(zip(nucleotides,counts))
    return (counted_nucleotides)

def DNAtoRNA(DNA):
    RNA=DNA.replace("T","U")
    return RNA

#Reverse order of a pattern
#input: Pattern
#output: reverse of the pattern
def Reverse(Pattern):
    reverse = " "
    for char in Pattern:
        #correct order:
        #reverse = char+reverse
        #reverse order
        reverse = char+reverse
    return reverse

# Complement of your pattern
#input: pattern
#complement of a pattern
def Complement(Pattern):
    comp = ""
    for char in Pattern:
        if char == "A":
            comp=comp+"T"
        if char == "C":
            comp=comp+"G"
        if char == "G":
            comp=comp+"C"
        if char == "T":
            comp=comp+"A"
    return (comp)

#looking for the reverse compliment of a pattern in case the target DNA string of interest is on the other strand 
# Input: Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

#To solve the Rabbits and Recurrence Relations. This is the Fibonacci exercise. 
#Basically two pairs of rabits mate for one month and the following month they give birth to (k) number of rabits. 
#You are to find how many rabits are there at a specified month (n)
def Fibonacci_seq(n,k):
    imm=[1,0]
    mat=[0,1]
    while len(mat)<n+1:
        imm.append(mat[-1]*k)
        mat.append(mat[-1]+imm[-2])
    return mat[-1]

def GC_content(strands):
    GC_con=[]
    for strand in strands:
        print (len (strand))
        tot=strand.count("G")+strand.count("C")
        per=(tot/len(strand))*100
        GC_con.append(per)
    return GC_con
GC_contents=GC_content(strands)
def top_GC(genes,strands,GC_contents):
    ind = np.argmax(GC_contents)
    return genes[ind],GC_contents[ind]

def HammingDistance(p, q):
    count = 0
    text=p
    text2=q
    for i in range(len(p)):
        if text[i]!=text2[i]:
            count +=1
    return count
