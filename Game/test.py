fin=open("OBSTACLE.txt","r")
lst=fin.read().split("\n")
lst.remove("")
print(type(lst))
print(lst)
fin.close()