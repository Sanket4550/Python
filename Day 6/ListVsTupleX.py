#               List   Tuple
#-------------------------------
#Ordered        yes     yes
#Indexed        yes     yes
#Mutable        yes     no
#Heterogeneous  yes     yes
#-------------------------------
def main():
   data1 = [10,3.14,True,"Pune"] #list
   data2 = (10,3.14,True,"Pune") #tuple

   print(data1)
   print(data2)

   print(data1[1])
   print(data2[1])


if __name__ == "__main__":
    main()
