plata=int(input("kolika ti je plata"))
if plata<100000: 
    print("plata ti je",plata)
elif plata>=100000 and plata<200000:
    print("plata ti je ",plata-(plata//5))
elif plata>=200000 and plata<300000:
    print("plata ti je ",plata-(plata//10))
else:
    print("plata ti je ",plata-(plata//20))
    
