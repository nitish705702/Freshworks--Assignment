import headerfile as head 
head. create("Nitish",25) 
head. read("Nitish")
head. create("Nitish",50)
head. modify("Nitish",55)
head. delete("Nitish")

test=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
test.start()
test.sleep()