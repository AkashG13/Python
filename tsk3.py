word=[];
print("Enter 3 Words in list: ")
c=3;
for i in range(c) :
    
    data=str(input())
    word.append(data)
    #n+1;
l=word[0]
for i in range(1,3):
    if (len(word[i])>len(l)):
        l=word[i]
print("Longest Word in list is: "+l)
        
 
