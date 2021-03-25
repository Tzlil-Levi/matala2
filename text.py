def revword(word:str)-> str:
    word= list(word)
    i = 0
    j = len(word)-1
    while i < int(len(word)/2):
        temp = word[i]
        word[i] = word[j]
        word[j] = temp
        i+=1
        j-=1
    word="".join(word).lower()
    return word

def countword()->int:
    file= open('text.txt','r')
    word= file.readline()
    word=word.lower()
    word=word.rstrip()
    counter=1
    
    for line in file:
        line=line.rstrip()
        list1=line.split(' ')
        for node in list1:
            node=revword(node)
            if node == word:
                counter+=1
    return counter