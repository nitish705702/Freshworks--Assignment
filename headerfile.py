import time as tm 
from threading import*

arr={}

def read(key):
    if(key not in arr):
        print("Error : Key does not Exist")
    else:
        brr=arr[key]
        if(b[1]!=0):
            if(tm.time()<b[1]):
                s=str(key)+":"+str(b[0]) 
                return s
            else:
                print("Error Key ",key,"has expired")
        else:
            s=str(key)+":"+str(b[0])
            return s


def modify(key,value):
    brr=arr[key]
    if(brr[1]!=0):
        if(tm.time()<brr[1]):
            if(key not in arr):
                print("Error : Key does not Exist") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                arr[key]=l
        else:
            print("Error Key ",key,"has expired") 
    else:
        if(key not in arr):
            print("Error : Key does not Exist")
        else:
            crr=[]
            crr.append(value)
            crr.append(brr[1])
            arr[key]=crr


def delete(key):
    if(key not in arr):
        print("Error : Key does not Exist ")
    else:
        brr=arr[key]
        if(brr[1] is not 0):
            if(tm.time()<brr[1]):
                del arr[key]
                print("Successfully delete")
            else:
                print("Error Key ",key,"has expired")
        else:
            del arr[key]
            print("Successfully delete")

def create(key,value,timeout=0):
    if(key in arr):
        print("Error : Key does not Exist") 
    else:
        if(key.isalpha()):
            x=1024*1020*1024 #constraints for file size less than 1GB
            y=1024*16*1024 #Jasonobject value less than 16KB
            if(len(d)<x and value<=y): 
                if(timeout==0):
                    l=[value,timeout]
                else:
                    l=[value,tm.time()+ is_timeout]
                if(len(key)<=32): 
                    arr[key]=l
            else:
                print("Memory limit exceeded")
        else:
            print("Invalid")
