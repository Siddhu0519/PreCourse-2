# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    p=arr[high]
    i=low-1
    for m in range(low,high):
        if arr[m]<=p:
            i=i+1
            arr[i],arr[m]=arr[m],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1


# Function to do Quick sort 
def quickSort(arr,low,high):
    part=partition(arr,low,high)
    quickSort(arr,low,part-1)
    quickSort(arr,part+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
