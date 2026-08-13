def myfun1(**hello): # key value pair input [dictionary] **kwargs
    for k,v in hello.items():
        print("Key-> ", k)
        print("Values-> ", v)
        print("")

myfun1(Name="Peter Parker", Age=25, City="New York", Identity= "Spider-Man")