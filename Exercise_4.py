# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr)>1:
        midle=len(arr)//2
        Lf=arr[:midle]
        Rg=arr[midle:]
        mergeSort(Lf)
        mergeSort(Rg)
        i=j=k=0
        while i<len(Lf) and j<len(Rg):
            if Lf[i]<Rg[j]:
                arr[k]=Lf[i]
                i+=1
            else:
                arr[k]=Rg[j]
                j+=1
            k+=1
        while i<len(Lf):
            arr[k]=Lf[i]
            i+=1
            k+=1
        while j<len(Rg):
            arr[k]=Rg[j]
            j+=1
            k+=1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
